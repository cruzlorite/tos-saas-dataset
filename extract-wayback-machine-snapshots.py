#!/bin/python3
# This file collects the data from The Wayback Machine for a given URL from the year specified by the user.
# Usage: python3 extract-wayback-machine-snapshots.py -u <URL> -y <YEAR> -o <OUTPUT_FOLDER>

import os
import time
import tqdm

from selenium import webdriver
from selenium.webdriver.common.by import By


def wayback_machine_snapshots(driver, url, year, wait_time=5):
    """This function retrieves the snapshots of a given URL in a given year.
    Args:
        driver: Selenium WebDriver
        url: URL to extract the snapshots from
        year: Year to retrieve the snapshots from
        wait_time: Time to wait before retrieving the HTML content
    """
    wayback_machine_url = f"https://web.archive.org/web/{year}0101000000*/{url}"
    driver.get(wayback_machine_url)
    time.sleep(wait_time)
    
    # snapshot selector
    selector = "div.calendar-day > a"
    snapshot_urls = [snapshot.get_attribute("href") for snapshot in driver.find_elements(By.CSS_SELECTOR, selector)]
    
    return snapshot_urls

def wayback_machine_fetch_snapshot(driver, snapshot_url, wait_time=20):
    """This function retrieves the HTML content of a snapshot URL
    Args:
        driver: Selenium WebDriver
        snapshot_url: URL of the snapshot
        wait_time: Time to wait before retrieving the HTML content
    """
    driver.get(snapshot_url)
    time.sleep(wait_time)
    return driver.page_source

def keep_one_snapshot_per_month(snapshots):
    """Keep one snapshot per month"""
    months = set()
    snapshots_to_keep = []
    for snapshot in snapshots:
        month = snapshot.split("/")[4][:6]
        if month not in months:
            months.add(month)
            snapshots_to_keep.append(snapshot)
    return snapshots_to_keep

def create_path_if_not_exists(path):
    """Create a path if it does not exist"""
    if not os.path.exists(path):
        os.makedirs(path)

def parse_args():
    """Parse the arguments of the script"""
    import argparse
    parser = argparse.ArgumentParser(description="Generate dataset with snapshots extracted from Wayback Machine for the given URL.")
    parser.add_argument("-u", "--url", type=str, help="URL to extract the snapshots from.")
    parser.add_argument("-y", "--year", type=int, default=2019, help="Year to retrieve the snapshots from.")
    parser.add_argument("-o", "--output", type=str, help="Output folder to save the HTML content.")
    parser.add_argument("--one-per-month", action="store_true", help="Retrieve one snapshot per month.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    
    # get current year
    current_year = time.localtime().tm_year
    
    # get snapshots
    snapshots = []
    for year in range(args.year, current_year+1):
        year_snapshots = wayback_machine_snapshots(driver, args.url, year)
        print(f"Found {len(year_snapshots)} snapshots for {year}.")
        snapshots += year_snapshots
    
    # keep one snapshot per month
    if args.one_per_month:
        snapshots = keep_one_snapshot_per_month(snapshots)
    
    print(f"Found {len(snapshots)} snapshots.")

    # iterate over snapshots tqdm
    for snapshot in tqdm.tqdm(snapshots):
        try:
            site_name = args.url.replace("http://", "").replace("https://", "").split("/")[0]
            snapshot_id = snapshot.replace("https://web.archive.org/web/", "").split("/")[0]
            
            output_file = f"{os.path.join(args.output, snapshot_id)}.html"
            if not os.path.exists(output_file):
                html_content = wayback_machine_fetch_snapshot(driver, snapshot)
                create_path_if_not_exists(args.output)
                with open(output_file, "w") as f:
                    f.write(html_content)
            else:
                print(f"Snapshot {snapshot} already exists.")
        except Exception as e:
            print(f"Error fetching snapshot {snapshot}.")
            import traceback
            print(traceback.format_exc())

    driver.quit()