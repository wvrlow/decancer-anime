#!/usr/bin/env python3
"""
This script is designed to clean up and rename video files and directories in a specified directory."
"""

import os
import re
import sys
from pathlib import Path

# Function to extract year from filename
def extract_year(name):
    year_match = re.search(r'\((\d{4})\)', name)
    return year_match.group(1) if year_match else None

def clean_name(name):
    year = extract_year(name)
    
    name = re.sub(r'\[.*?\]|\(.*?\)|\{.*?\}', '', name).strip()
    name = re.sub(r'\b(2160p|1080p|720p|480p|4K|UHD|2K|FLAC2\.0|AAC|DDP5\.1|DDP2\.0|x265|x264|HEVC|HDR|BDRip|WEBRip|BluRay|Dual Audio|10bit|10-Bit|10 bits|10 bit|8bit|8-Bit|12bit|12-Bit|AVC|AAC|E-AC-3|TV \+ SP|H\.264|H\.265|VP9|AV1|HDR10|HDR10\+|Dolby Vision|SDR|OPUS|MP3|EAC3|LPCM|TrueHD|REMUX|HDTV|DVDRip|WebDL|Web-DL|Mini Encode|BD|UHD BD|AC3|DTS|DTS-HD|ATMOS|5\.1|7\.1|2\.0)\b', '', name, flags=re.IGNORECASE).strip() # Remove common video/audio formats and technical terms
    name = re.sub(r'\b(SubsPlease|NakayubiSubs|HorribleSubs|Judas|EMBER|FFF|Commie|AnimeRG|THORA|SSA|VARYG|AniDub|Coalgirls|GJM|Aruri|VCB-Studio|ohys|darkstar|CTR|MTBB|UTW|GIGA|Reinforce|PAS|LostYears|YURASUKA|Anime Time|DB|Beatrice-Raws|Moozzi2|neoHEVC|Tenrai-Sensei|Nyanpasu|Reaktor|smplstc|Sokudo|Dae|YuushaNi|Cleo|Prof|CookieSubs|weeaboo gamer girl|Tsundere-Raws)\b|[A-Za-z]+-Raws', '', name, flags=re.IGNORECASE).strip()  # Remove known release groups
    name = re.sub(r'\b(WEB|WEBDL)\b', '', name).strip()  # Remove sources
    name = re.sub(r'\s*\d+-\d+\s*\bBatch\b', '', name).strip()  # Handle "1-12 Batch" pattern
    name = re.sub(r'\bDD\b', '', name).strip()  # Remove standalone "DD"
    name = re.sub(r'[-_\.]+$', '', name).strip()  # Remove trailing hyphens, underscores, and dots
    name = re.sub(r'\s-\s(?=\.)', ' ', name).strip()  # remove trailing hyphen between spaces when followed by a dot
    name = re.sub(r'[\s_]+(\.mkv|\.mp4|\.avi|\.mov|\.flv|\.wmv|\.m4v|\.mpg|\.mpeg|\.webm|\.vob|\.ogv|\.3gp|\.3g2|\.mxf|\.m2ts|\.mts|\.ts|\.divx|\.xvid|\.rm|\.rmvb|\.asf|\.amv|\.m2v|\.svi|\.yuv|\.mpe|\.mpv|\.mkv|\.mp4)$', r'\1', name).strip() # remove trailing space and underscore before file extensions
    name = re.sub(r'[._\-\s]+-\s*(?=\.(mkv|mp4|avi|mov|flv|wmv|m4v|mpg|mpeg|webm|vob|ogv|3gp|3g2|mxf|m2ts|mts|ts|divx|xvid|rm|rmvb|asf|amv|m2v|svi|yuv|mpe|mpv))', '', name).strip()  # remove trailing special chars and hyphen before video extension
    name = re.sub(r'_-_', ' ', name).strip() # replace "_-_" with space
    name = re.sub(r'\s+', ' ', name).strip()
    
    # Restore year if it was present
    if year:
        episode_match = re.search(r'\s+-\s+\d+', name)
        extension_match = re.search(r'\.(mkv|mp4|avi|mov|flv|wmv|m4v|mpg|mpeg|webm|vob|ogv|3gp|3g2|mxf|m2ts|mts|ts|divx|xvid|rm|rmvb|asf|amv|m2v|svi|yuv|mpe|mpv)$', name)
        
        if episode_match:
            insert_pos = episode_match.start()
            name = name[:insert_pos] + f" ({year})" + name[insert_pos:]
        elif extension_match:
            insert_pos = extension_match.start()
            name = name[:insert_pos] + f" ({year})" + name[insert_pos:]
        else:
            name = name + f" ({year})"
    
    return name

# Function to preview changes and confirm
def preview_and_confirm_changes(changes):
    if not changes:
        print("No changes to make.")
        return False
    
    print("\n======= PREVIEW OF CHANGES =======")
    print(f"Number of changes: {len(changes)}")
    
    file_changes = [(old, new) for old, new, is_dir in changes if not is_dir]
    dir_changes = [(old, new) for old, new, is_dir in changes if is_dir]
    
    if dir_changes:
        print("\nDIRECTORY CHANGES:")
        for i, (old_path, new_path) in enumerate(dir_changes, 1):
            print(f"{i}. FROM: {old_path}")
            print(f"   TO:   {new_path}")
            if i >= 10 and len(dir_changes) > 15:
                print(f"... and {len(dir_changes) - 10} more directory changes")
                break
    
    if file_changes:
        print("\nFILE CHANGES:")
        for i, (old_path, new_path) in enumerate(file_changes, 1):
            print(f"{i}. FROM: {old_path}")
            print(f"   TO:   {new_path}")
            if i >= 20 and len(file_changes) > 25:
                print(f"... and {len(file_changes) - 20} more file changes")
                break
    
    print("\n=================================")
    
    while True:
        response = input("\nApply these changes? (y/N) or (s) to show all: ").strip().lower()
        if response == 'y':
            return True
        elif response == '' or response == 'n':
            return False
        elif response == 's':
            print("\n================ ALL CHANGES ================\n")
            
            # Print directories first
            if any(is_dir for _, _, is_dir in changes):
                print("\n--- DIRECTORIES ---\n")
                dir_count = 1
                for old_path, new_path, is_dir in changes:
                    if is_dir:
                        print(f"{dir_count:3d}. FROM: {old_path}")
                        print(f"     TO:   {new_path}")
                        print()
                        dir_count += 1
            
            # Then print files
            if any(not is_dir for _, _, is_dir in changes):
                print("\n--- FILES ---\n")
                file_count = 1
                for old_path, new_path, is_dir in changes:
                    if not is_dir:
                        print(f"{file_count:3d}. FROM: {old_path}")
                        print(f"     TO:   {new_path}")
                        print()
                        file_count += 1
            
            print("\n===========================================")
        else:
            print("Please press 'y' to proceed, 'N' or Enter to cancel, or 's' to show all changes")

# Function to clean the directory
def clean_directory(directory):
    video_extensions = ['.mkv', '.mp4', '.avi', '.mov', '.flv', '.wmv', '.m4v', '.mpg', '.mpeg', '.webm', '.vob', '.ogv', '.3gp', '.3g2', '.mxf', '.m2ts', '.mts', '.ts', '.divx', '.xvid', '.rm', '.rmvb', '.asf', '.amv', '.m2v', '.svi', '.yuv', '.mpe', '.mpv']
    changes = []
    
    # First, collect all potential changes
    for root, dirs, files in os.walk(directory):
        for name in dirs:
            old_path = Path(root) / name
            new_name = clean_name(name)
            new_path = Path(root) / new_name
            if old_path != new_path:
                changes.append((old_path, new_path, True))  # True indicates directory

        for name in files:
            file_ext = os.path.splitext(name)[1].lower()
            # only process video files
            if file_ext in video_extensions:
                old_path = Path(root) / name
                new_name = clean_name(name)
                new_path = Path(root) / new_name
                if old_path != new_path:
                    changes.append((old_path, new_path, False))  # False indicates file

    # Sort directories by depth to rename deepest last
    changes.sort(key=lambda x: (x[2], -len(x[0].parts) if x[2] else 0))  # Sort directories by depth, files first
    
    # Show preview and get confirmation
    if preview_and_confirm_changes(changes):
        # Apply changes
        files_renamed = 0
        dirs_renamed = 0
        errors = 0
        
        # First rename files
        for old_path, new_path, is_dir in changes:
            if not is_dir:
                try:
                    old_path.rename(new_path)
                    files_renamed += 1
                    print(f"Renamed file: {old_path} -> {new_path}")
                except OSError as e:
                    errors += 1
                    print(f"Error renaming file: {old_path} to {new_path} - {e}")

        # Then rename directories in reverse depth order
        dir_changes = [(old, new) for old, new, is_dir in changes if is_dir]
        dir_changes.sort(key=lambda x: len(x[0].parts), reverse=True)  # Sort by depth, deepest first
        
        for old_path, new_path in dir_changes:
            try:
                old_path.rename(new_path)
                dirs_renamed += 1
                print(f"Renamed directory: {old_path} -> {new_path}")
            except OSError as e:
                errors += 1
                print(f"Error renaming directory: {old_path} to {new_path} - {e}")

        print(f"\nSummary: {files_renamed} files and {dirs_renamed} directories renamed. {errors} errors occurred.")
    else:
        print("Operation cancelled. No changes were made.")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = '.'
    clean_directory(directory)
    print("Done!")
