#!/usr/bin/env python3
"""
This script is designed to clean up and rename video files and directories in a specified directory.
"""

import os
import re
import sys
import datetime
from pathlib import Path

def clean_name(name, is_file=True):
    name = re.sub(r'\(\s*[^()]*(?:2160p|1280|1080|1080p|720p|540p|480p|4K|UHD|2K|FLAC|AAC|DDP|x265|H265|x264|HEVC|HDR|BDRip|WEBRip|BluRay|Menu)[^()]*\)', '', name, flags=re.IGNORECASE)  # Remove parentheses containing technical terms
    name = re.sub(r'\[\s*[^\[\]]*(?:2160p|1280|1080|1080p|720p|480p|540|4K|UHD|2K|FLAC|AAC|DDP|x265|x264|HEVC|HDR|BDRip|WEBRip|BluRay|v2|v1|v3|fixed)[^\[\]]*\]', '', name, flags=re.IGNORECASE)  # Remove brackets containing technical terms
    name = re.sub(r'\b(2160p|1080p|720p|480p|4K|UHD|2K|FLAC[0-9]\.[0-9]|FLAC|AAC(?:[0-9]\.[0-9])?|DDP[0-9]\.[0-9]|DDP[0-9]|DDP|DD[0-9]\.[0-9]|DD[0-9]|H265|x265|x264|HEVC|HDR|BDRip|BrRip|WEBRip|Complete|BluRay|Dual Audio|10bit|10-Bit|10 bits|10 bit|8bit|8-Bit|12bit|12-Bit|AVC|AAC|E-AC-3|TV \+ SP|H\.264|H\.265|VP9|AV1|HDR10|HDR10\+|Dolby Vision|SDR|OPUS|MP3|EAC3|LPCM|TrueHD|REMUX|HDTV|DVDRip|WebDL|Web-DL|Mini Encode|Dual-Audio|BD|UHD BD|AC3|DTS|DTSHD|DTS-HD|ATMOS|5\.1|7\.1|2\.0)\b', '', name, flags=re.IGNORECASE).strip() # Remove common video/audio formats and technical terms
    name = re.sub(r'\b(SubsPlease|MSubs|NakayubiSubs|HorribleSubs|Judas|EMBER|FFF|Commie|AnimeRG|THORA|SSA|VARYG|AniDub|Coalgirls|GJM|Aruri|VCB-Studio|ohys|darkstar|CTR|MTBB|UTW|GIGA|Reinforce|PAS|LostYears|YURASUKA|Anime Time|DB|Beatrice-Raws|Moozzi2|neoHEVC|Tenrai-Sensei|Nyanpasu|Reaktor|smplstc|Sokudo|Dae|YuushaNi|Cleo|Prof|CookieSubs|weeaboo gamer girl|Tsundere-Raws|ToonsHub)\b|[A-Za-z]+-Raws', '', name, flags=re.IGNORECASE).strip()  # Remove known release groups
    name = re.sub(r'\[\s*[0-9A-F]{8}\s*\]', '', name, flags=re.IGNORECASE)  # Remove brackets containing 8-character hex hash
    name = re.sub(r'\[(?![^\]]*\d)[^\]]*\]', '', name).strip()  # Remove brackets that don't contain numbers
    name = re.sub(r'\b(WEB|WEBDL|AMZN|DUAL|CUSTOM|RM4K|Criterion|Paso77|YIFY)\b|(-WiKi|-NOGRP|-SLOT|-EbP|-P2P|MA-SARTRE)', '', name).strip()  # Remove sources and other terms
    name = re.sub(r'\s*\d+-\d+\s*\bBatch\b', '', name).strip()  # Handle "1-12 Batch" pattern
    name = re.sub(r'\bDD\+\b|\bDD\b', '', name).strip()  # Remove standalone "DD+" and "DD"
    name = re.sub(r'\b(ITA|ENG|JAP|SPA|GER|FRE|RUS)\b', '', name).strip()  # Remove language codes
    name = re.sub(r'\s*\+\s*Special', '', name, flags=re.IGNORECASE).strip()  # Remove "+ Special" occurrences
    name = re.sub(r'\s*\+\s*(Extras|Extra)', '', name, flags=re.IGNORECASE).strip()  # yeah
    name = re.sub(r'\s*\+\s*OVA', '', name, flags=re.IGNORECASE).strip()  # Remove "+OVA" occurrences
    name = re.sub(r'\(\s*\)||\[\s*\]', '', name).strip() # Remove empty parentheses and brackets
    name = re.sub(r'[-_\.]+$', '', name).strip()  # Remove trailing hyphens, underscores, and dots
    name = re.sub(r'\s-\s(?=\.)', ' ', name).strip()  # remove trailing hyphen between spaces when followed by a dot
    name = re.sub(r'[\s_]+(\.mkv|\.mp4|\.avi|\.mov|\.flv|\.wmv|\.m4v|\.mpg|\.mpeg|\.webm|\.vob|\.ogv|\.3gp|\.3g2|\.mxf|\.m2ts|\.mts|\.ts|\.divx|\.xvid|\.rm|\.rmvb|\.asf|\.amv|\.m2v|\.svi|\.yuv|\.mpe|\.mpv)$', r'\1', name).strip()  # Fix spacing for video files
    name = re.sub(r'[._\-\s]+-\s*(?=\.(mkv|mp4|avi|mov|flv|wmv|m4v|mpg|mpeg|webm|vob|ogv|3gp|3g2|mxf|m2ts|mts|ts|divx|xvid|rm|rmvb|asf|amv|m2v|svi|yuv|mpe|mpv))', '', name).strip()  # Remove special chars before video extension
    name = re.sub(r'_-_', ' ', name).strip()  # Replace "_-_" with space
    name = re.sub(r'\s+', ' ', name).strip()  # Replace multiple spaces with a single space
    name = re.sub(r'(E\d+)v\d+', r'\1', name, flags=re.IGNORECASE).strip()  # Remove version indicators after episode numbers (E13v2)
    name = re.sub(r'\b(v[0-9]|v[0-9][0-9])\b(?=.*\.(mkv|mp4|avi|mov|flv|wmv|m4v|mpg|mpeg|webm|vob|ogv|3gp|3g2|mxf|m2ts|mts|ts|divx|xvid|rm|rmvb|asf|amv|m2v|svi|yuv|mpe|mpv))', '', name, flags=re.IGNORECASE).strip()  # Remove version indicators only if followed by video extension
    name = re.sub(r'\b(v[0-9]|v[0-9][0-9])\b$', '', name, flags=re.IGNORECASE).strip()  # Remove version indicators if at the end (for directories)
    name = re.sub(r'\.{2,}', '.', name).strip()  # Replace consecutive dots with a single dot
    name = re.sub(r'\s+(?=\.(mkv|mp4|avi|mov|flv|wmv|m4v|mpg|mpeg|webm|vob|ogv|3gp|3g2|mxf|m2ts|mts|ts|divx|xvid|rm|rmvb|asf|amv|m2v|svi|yuv|mpe|mpv)$)', '', name).strip() # Remove trailing space before video extension
    if not is_file:
        name = name.rstrip('.') # Remove trailing dot for directories
    return name

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

def clean_directory(directory):
    video_extensions = ['.mkv', '.mp4', '.avi', '.mov', '.flv', '.wmv', '.m4v', '.mpg', '.mpeg', '.webm', '.vob', '.ogv', '.3gp', '.3g2', '.mxf', '.m2ts', '.mts', '.ts', '.divx', '.xvid', '.rm', '.rmvb', '.asf', '.amv', '.m2v', '.svi', '.yuv', '.mpe', '.mpv']
    changes = []

    # First, collect all potential changes
    for root, dirs, files in os.walk(directory):
        for name in dirs:
            old_path = Path(root) / name
            new_name = clean_name(name, is_file=False)
            new_path = Path(root) / new_name
            if old_path != new_path:
                changes.append((old_path, new_path, True))  # True indicates directory

        for name in files:
            file_ext = os.path.splitext(name)[1].lower()
            # Only process video files
            if file_ext in video_extensions:
                old_path = Path(root) / name
                new_name = clean_name(name, is_file=True)
                new_path = Path(root) / new_name
                if old_path != new_path:
                    changes.append((old_path, new_path, False))  # False indicates file

    # Sort directories by depth to rename deepest last
    changes.sort(key=lambda x: (x[2], -len(x[0].parts) if x[2] else 0))  # Sort directories by depth, files first

    # Show preview and get confirmation
    if preview_and_confirm_changes(changes):
        files_renamed = 0
        dirs_renamed = 0
        errors = 0
        successful_changes = []
        failed_changes = []

        # First rename files
        for old_path, new_path, is_dir in changes:
            if not is_dir:
                try:
                    old_path.rename(new_path)
                    files_renamed += 1
                    print(f"Renamed file: {old_path} -> {new_path}")
                    successful_changes.append((str(old_path), str(new_path), "file"))
                except OSError as e:
                    errors += 1
                    print(f"Error renaming file: {old_path} to {new_path} - {e}")
                    failed_changes.append((str(old_path), str(new_path), "file", str(e)))

        # Then rename directories in reverse depth order
        dir_changes = [(old, new) for old, new, is_dir in changes if is_dir]
        dir_changes.sort(key=lambda x: len(x[0].parts), reverse=True)  # Sort by depth, deepest first

        for old_path, new_path in dir_changes:
            try:
                old_path.rename(new_path)
                dirs_renamed += 1
                print(f"Renamed directory: {old_path} -> {new_path}")
                successful_changes.append((str(old_path), str(new_path), "directory"))
            except OSError as e:
                errors += 1
                print(f"Error renaming directory: {old_path} to {new_path} - {e}")
                failed_changes.append((str(old_path), str(new_path), "directory", str(e)))

        print(f"\nSummary: {files_renamed} files and {dirs_renamed} directories renamed. {errors} errors occurred.")
        
        # Generate log file
        write_log_file(directory, successful_changes, failed_changes, files_renamed, dirs_renamed, errors)
    else:
        print("Operation cancelled. No changes were made.")

def write_log_file(directory, successful_changes, failed_changes, files_renamed, dirs_renamed, errors):
    """Write a detailed log of all changes to a file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = Path(directory) / f"decancer_changes_{timestamp}.log"
    
    try:
        with open(log_filename, 'w', encoding='utf-8') as logfile:
            logfile.write(f"Decancer Anime Renaming Log - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            logfile.write(f"Directory: {directory}\n\n")
            logfile.write(f"SUMMARY:\n")
            logfile.write(f"- Files renamed: {files_renamed}\n")
            logfile.write(f"- Directories renamed: {dirs_renamed}\n")
            logfile.write(f"- Errors: {errors}\n\n")
            
            if successful_changes:
                logfile.write("SUCCESSFUL CHANGES:\n")
                for i, (old_path, new_path, item_type) in enumerate(successful_changes, 1):
                    logfile.write(f"{i}. [{item_type.upper()}] FROM: {old_path}\n")
                    logfile.write(f"   TO: {new_path}\n\n")
            
            if failed_changes:
                logfile.write("\nFAILED CHANGES:\n")
                for i, (old_path, new_path, item_type, error_msg) in enumerate(failed_changes, 1):
                    logfile.write(f"{i}. [{item_type.upper()}] FROM: {old_path}\n")
                    logfile.write(f"   TO: {new_path}\n")
                    logfile.write(f"   ERROR: {error_msg}\n\n")
        
        print(f"\nLog file created: {log_filename}")
    except Exception as e:
        print(f"Error creating log file: {e}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = '.'
    clean_directory(directory)
    print("Done!")
