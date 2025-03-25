#!/usr/bin/env python3
"""
Generate test anime file structures for testing decancer.py.
This script only creates a test directory structure with common anime naming patterns.
"""

import os
import argparse
from pathlib import Path

def create_test_structure(root_dir: str) -> None:
    """Create a test directory structure for testing the cleaner."""
    test_root = Path(root_dir)
    
    # Create test directories based on animetree.txt
    dirs = [
        test_root / "[Anime Time] Assassination Classroom (Season 01+Season 02+Movie) [BD] [Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub] [Batch] (Ansatsu Kyoushitsu)",
        test_root / "[Anime Time] Assassination Classroom (Season 01+Season 02+Movie) [BD] [Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub] [Batch] (Ansatsu Kyoushitsu)" / "[Anime Time] Assassination Classroom Season 01",
        test_root / "[Anime Time] Assassination Classroom (Season 01+Season 02+Movie) [BD] [Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub] [Batch] (Ansatsu Kyoushitsu)" / "[Anime Time] Assassination Classroom Season 02",
        
        test_root / "[Anime Time] Death Parade + Special [BD][Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub]",
        
        test_root / "[Anime Time] K-On! (Season 01+02+Movie+OVA+Specials) [BD][Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub]",
        test_root / "[Anime Time] K-On! (Season 01+02+Movie+OVA+Specials) [BD][Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub]" / "[Anime Time] K-On!",
        test_root / "[Anime Time] K-On! (Season 01+02+Movie+OVA+Specials) [BD][Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub]" / "[Anime Time] K-On!" / "NC",
        test_root / "[Anime Time] K-On! (Season 01+02+Movie+OVA+Specials) [BD][Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub]" / "[Anime Time] K-On!! (Season 2)",
        test_root / "[Anime Time] K-On! (Season 01+02+Movie+OVA+Specials) [BD][Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub]" / "[Anime Time] K-On! The Movie",
        
        test_root / "[Beatrice-Raws] Suzume no Tojimari [BDRip 3840x1608 HEVC HDR DTSHD]",
        test_root / "[Beatrice-Raws] Suzume no Tojimari [BDRip 3840x1608 HEVC HDR DTSHD]" / "Audio_bonus",
        test_root / "[Beatrice-Raws] Suzume no Tojimari [BDRip 3840x1608 HEVC HDR DTSHD]" / "BD menu",
        
        test_root / "Bocchi.the.Rock.S01.1080p.BluRay.10-Bit.FLAC2.0.x265-YURASUKA",
        test_root / "Deatte 5-byou de Battle S01 1080p Dual Audio WEBRip AAC x265-EMBER",
        
        test_root / "[Anime Time] Hunter x Hunter (Series) 2011 [Dual Audio][BD][1080p][HEVC 10bit x265][AAC][Eng Sub] [Batch]",
        test_root / "[Anime Time] Hunter x Hunter (Series) 2011 [Dual Audio][BD][1080p][HEVC 10bit x265][AAC][Eng Sub] [Batch]" / "Hunter X Hunter Movies",
        
        test_root / "Ano Hi Mita Hana no Namae wo Bokutachi wa Mada Shiranai [BD]",
        test_root / "Ano Hi Mita Hana no Namae wo Bokutachi wa Mada Shiranai [BD]" / "Extras",
        
        test_root / "Another S01+OVA 1080p Dual Audio BDRip 10 bits DD x265-EMBER",
        
        test_root / "[Beatrice-Raws] Tenki no Ko [BDRip 3840x2160 HEVC HDR DTSHD]",
        test_root / "[Beatrice-Raws] Tenki no Ko [BDRip 3840x2160 HEVC HDR DTSHD]" / "Audio 5.1",
        test_root / "[Beatrice-Raws] Tenki no Ko [BDRip 3840x2160 HEVC HDR DTSHD]" / "Audio Guide",
        test_root / "[Beatrice-Raws] Tenki no Ko [BDRip 3840x2160 HEVC HDR DTSHD]" / "BD menu",
        
        test_root / "Bungou Stray Dogs",
        test_root / "Bungou Stray Dogs" / "Bungou Stray Dogs",
        test_root / "Bungou Stray Dogs" / "Bungou Stray Dogs" / "Extras",
        test_root / "Bungou Stray Dogs" / "Bungou Stray Dogs 2nd Season",
        test_root / "Bungou Stray Dogs" / "Bungou Stray Dogs 2nd Season" / "Extras",
        test_root / "Bungou Stray Dogs" / "Bungou Stray Dogs 3rd Season",
        test_root / "Bungou Stray Dogs" / "Bungou Stray Dogs Dead Apple",
        
        test_root / "Charlotte [BD][1080p][HEVC 10bit x265][Dual Audio][Tenrai-Sensei]",
        test_root / "Charlotte [BD][1080p][HEVC 10bit x265][Dual Audio][Tenrai-Sensei]" / "Season 1",
        test_root / "Charlotte [BD][1080p][HEVC 10bit x265][Dual Audio][Tenrai-Sensei]" / "Specials",
        
        test_root / "[CookieSubs] THE IDOLM@STER Cinderella Girls [BD 1080p HEVC FLAC]",
        test_root / "[CookieSubs] THE IDOLM@STER Cinderella Girls [BD 1080p HEVC FLAC]" / "S1",
        test_root / "[CookieSubs] THE IDOLM@STER Cinderella Girls [BD 1080p HEVC FLAC]" / "S2",
        test_root / "[CookieSubs] THE IDOLM@STER Cinderella Girls [BD 1080p HEVC FLAC]" / "Special",
        
        test_root / "Danganronpa Complete Package [Presented By EMBER]",
        test_root / "Danganronpa Complete Package [Presented By EMBER]" / "01.Danganronpa The Animation S01 1080p Dual Audio BDRip 10 bits DD x265-EMBER",
        test_root / "Danganronpa Complete Package [Presented By EMBER]" / "02.Danganronpa 3 Future Arc 1080p Dual Audio BDRip 10 bits DD x265-EMBER",
        test_root / "Danganronpa Complete Package [Presented By EMBER]" / "03.Danganronpa 3 Despair Arc 1080p Dual Audio BDRip 10 bits DD x265-EMBER",
        test_root / "Danganronpa Complete Package [Presented By EMBER]" / "04.Danganronpa 3 Hope Arc 1080p Dual Audio BDRip 10 bits DD x265-EMBER",
        
        test_root / "Hibike! Euphonium",
        test_root / "Hibike! Euphonium" / "Hibike! Euphonium",
        test_root / "Hibike! Euphonium" / "Hibike! Euphonium" / "Extras",
        test_root / "Hibike! Euphonium" / "Hibike! Euphonium 2",
        test_root / "Hibike! Euphonium" / "Hibike! Euphonium 2" / "Extras",
        test_root / "Hibike! Euphonium" / "Hibike! Euphonium Movies",
        
        test_root / "[Moozzi2] Girls Band Cry [ x265-10Bit Ver. ] - TV + SP",
        test_root / "[Moozzi2] Girls Band Cry [ x265-10Bit Ver. ] - TV + SP" / "EXTRA",
        test_root / "[Moozzi2] Girls Band Cry [ x265-10Bit Ver. ] - TV + SP" / "EXTRA" / "[SP12] Bonus CD",
        test_root / "[Moozzi2] Girls Band Cry [ x265-10Bit Ver. ] - TV + SP" / "EXTRA" / "[SP13] BD Scans",
        test_root / "[Moozzi2] Girls Band Cry [ x265-10Bit Ver. ] - TV + SP" / "ScreenShot",
        
        test_root / "No Game No Life [BD][1080p][HEVC 10bit x265][Dual Audio][Tenrai-Sensei]",
        test_root / "No Game No Life [BD][1080p][HEVC 10bit x265][Dual Audio][Tenrai-Sensei]" / "Other",
        test_root / "No Game No Life [BD][1080p][HEVC 10bit x265][Dual Audio][Tenrai-Sensei]" / "Season 1",
        test_root / "No Game No Life [BD][1080p][HEVC 10bit x265][Dual Audio][Tenrai-Sensei]" / "Specials",
        test_root / "No Game No Life [BD][1080p][HEVC 10bit x265][Dual Audio][Tenrai-Sensei]" / "Trailers",
        
        test_root / "[Nyanpasu] Idoly Pride 1-12 Batch [v2][BD][1080p][HEVC][FLAC]",
        test_root / "[Nyanpasu] Idoly Pride 1-12 Batch [v2][BD][1080p][HEVC][FLAC]" / "EXTRAS",
        test_root / "[Nyanpasu] Idoly Pride 1-12 Batch [v2][BD][1080p][HEVC][FLAC]" / "EXTRAS" / "MENU",
        test_root / "[Nyanpasu] Idoly Pride 1-12 Batch [v2][BD][1080p][HEVC][FLAC]" / "EXTRAS" / "Scans",
        test_root / "[Nyanpasu] Idoly Pride 1-12 Batch [v2][BD][1080p][HEVC][FLAC]" / "EXTRAS" / "Scans" / "VOL1",
        test_root / "[Nyanpasu] Idoly Pride 1-12 Batch [v2][BD][1080p][HEVC][FLAC]" / "EXTRAS" / "Scans" / "VOL2",
        test_root / "[Nyanpasu] Idoly Pride 1-12 Batch [v2][BD][1080p][HEVC][FLAC]" / "EXTRAS" / "Scans" / "VOL3",
        
        test_root / "[Sokudo] The Melancholy of Haruhi Suzumiya 2006+2009+Movie [1080p BD][AV1][dual audio]",
        test_root / "[Sokudo] The Melancholy of Haruhi Suzumiya 2006+2009+Movie [1080p BD][AV1][dual audio]" / "2006",
        test_root / "[Sokudo] The Melancholy of Haruhi Suzumiya 2006+2009+Movie [1080p BD][AV1][dual audio]" / "2009",
        test_root / "[Sokudo] The Melancholy of Haruhi Suzumiya 2006+2009+Movie [1080p BD][AV1][dual audio]" / "Movie",
        
        test_root / "Wonder Egg Priority (BDRip 1080p HEVC FLAC) [Dae]",
        test_root / "Wonder Egg Priority (BDRip 1080p HEVC FLAC) [Dae]" / "Extras",
        test_root / "Wonder Egg Priority (BDRip 1080p HEVC FLAC) [Dae]" / "Extras" / "Fonts",
        test_root / "Wonder Egg Priority (BDRip 1080p HEVC FLAC) [Dae]" / "Extras" / "NCs",
        test_root / "Wonder Egg Priority (BDRip 1080p HEVC FLAC) [Dae]" / "Extras" / "Subtitles",
        test_root / "Wonder Egg Priority (BDRip 1080p HEVC FLAC) [Dae]" / "Specials",
        
        test_root / "Zombie.Land.Saga.S01.v2.1080p.BluRay.10-Bit.Dual-Audio.FLAC5.1.x265-YURASUKA",
        test_root / "Zombie.Land.Saga.S02.1080p.BluRay.10-Bit.Dual-Audio.FLAC5.1.x265-YURASUKA",
    ]
    
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
    
    # Create test files based on animetree.txt
    files = [
        # Assassination Classroom
        (test_root / "[Anime Time] Assassination Classroom (Season 01+Season 02+Movie) [BD] [Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub] [Batch] (Ansatsu Kyoushitsu)" / "[Anime Time] Assassination Classroom Season 01" / "[Anime Time] Assassination Classroom - 01.mkv", ""),
        (test_root / "[Anime Time] Assassination Classroom (Season 01+Season 02+Movie) [BD] [Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub] [Batch] (Ansatsu Kyoushitsu)" / "[Anime Time] Assassination Classroom Season 01" / "[Anime Time] Assassination Classroom - 22.mkv", ""),
        (test_root / "[Anime Time] Assassination Classroom (Season 01+Season 02+Movie) [BD] [Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub] [Batch] (Ansatsu Kyoushitsu)" / "[Anime Time] Assassination Classroom Season 02" / "[Anime Time] Assassination Classroom Season 02 - 01.mkv", ""),
        (test_root / "[Anime Time] Assassination Classroom (Season 01+Season 02+Movie) [BD] [Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub] [Batch] (Ansatsu Kyoushitsu)" / "[Anime Time] Assassination Classroom The Movie 365 Days.mkv", ""),
        
        # Death Parade
        (test_root / "[Anime Time] Death Parade + Special [BD][Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub]" / "Death Parade - 01.mkv", ""),
        (test_root / "[Anime Time] Death Parade + Special [BD][Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub]" / "Death Parade - 12.mkv", ""),
        (test_root / "[Anime Time] Death Parade + Special [BD][Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub]" / "Death Parade Special.mkv", ""),

        # K-On!
        (test_root / "[Anime Time] K-On! (Season 01+02+Movie+OVA+Specials) [BD][Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub]" / "[Anime Time] K-On!" / "[Anime Time] K-On! - 01.mkv", ""),
        (test_root / "[Anime Time] K-On! (Season 01+02+Movie+OVA+Specials) [BD][Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub]" / "[Anime Time] K-On!" / "[Anime Time] K-On! - OVA.mkv", ""),
        (test_root / "[Anime Time] K-On! (Season 01+02+Movie+OVA+Specials) [BD][Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub]" / "[Anime Time] K-On!! (Season 2)" / "[Anime Time] K-On!! - 01.mkv", ""),
        (test_root / "[Anime Time] K-On! (Season 01+02+Movie+OVA+Specials) [BD][Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub]" / "[Anime Time] K-On! The Movie" / "[Anime Time] K-ON! The Movie.mkv", ""),

        # Suzume
        (test_root / "[Beatrice-Raws] Suzume no Tojimari [BDRip 3840x1608 HEVC HDR DTSHD]" / "[Beatrice-Raws] Suzume no Tojimari [BDRip 3840x1608 HEVC HDR DTSHD].mkv", ""),
        (test_root / "[Beatrice-Raws] Suzume no Tojimari [BDRip 3840x1608 HEVC HDR DTSHD]" / "Audio_bonus" / "[Beatrice-Raws] Suzume no Tojimari [BDRip 1920x804 HEVC DTSHD]_Audio_51.mka", ""),
        (test_root / "[Beatrice-Raws] Suzume no Tojimari [BDRip 3840x1608 HEVC HDR DTSHD]" / "BD menu" / "BD Menu 01.png", ""),

        # Additional test files
        (test_root / "Bocchi.the.Rock.S01.1080p.BluRay.10-Bit.FLAC2.0.x265-YURASUKA" / "Bocchi.the.Rock.S01E01.1080p.BluRay.10-Bit.FLAC2.0.x265-YURASUKA.mkv", ""),
        (test_root / "Deatte 5-byou de Battle S01 1080p Dual Audio WEBRip AAC x265-EMBER" / "S01E01-Sophist.mkv", ""),
        (test_root / "Bocchi the Rock! Re (2024) 1080p WEB x264 E-AC-3 -Tsundere-Raws (CUSTOM).mkv", ""),
        (test_root / "Bocchi the Rock! Re Re (2024) 1080p WEB x264 E-AC-3 -Tsundere-Raws (CUSTOM).mkv", ""),
        
        # Hunter x Hunter
        (test_root / "[Anime Time] Hunter x Hunter (Series) 2011 [Dual Audio][BD][1080p][HEVC 10bit x265][AAC][Eng Sub] [Batch]" / "Hunter x Hunter (2011) - 001.mkv", ""),
        (test_root / "[Anime Time] Hunter x Hunter (Series) 2011 [Dual Audio][BD][1080p][HEVC 10bit x265][AAC][Eng Sub] [Batch]" / "Hunter x Hunter (2011) - 148.mkv", ""),
        (test_root / "[Anime Time] Hunter x Hunter (Series) 2011 [Dual Audio][BD][1080p][HEVC 10bit x265][AAC][Eng Sub] [Batch]" / "Hunter X Hunter Movies" / "Hunter X Hunter - Phantom Rouge.mkv", ""),
        (test_root / "[Anime Time] Hunter x Hunter (Series) 2011 [Dual Audio][BD][1080p][HEVC 10bit x265][AAC][Eng Sub] [Batch]" / "Hunter X Hunter Movies" / "Hunter X Hunter - The Last Mission.mkv", ""),
        
        # Anohana
        (test_root / "Ano Hi Mita Hana no Namae wo Bokutachi wa Mada Shiranai [BD]" / "[DB]Ano Hi Mita Hana no Namae wo Bokutachi wa Mada Shiranai._-_01_(Dual Audio_10bit_BD1080p_x265).mkv", ""),
        (test_root / "Ano Hi Mita Hana no Namae wo Bokutachi wa Mada Shiranai [BD]" / "Extras" / "[DB]Ano Hi Mita Hana no Namae wo Bokutachi wa Mada Shiranai. Movie_-_(10bit_BD1080p_x265).mkv", ""),
        
        # Another
        (test_root / "Another S01+OVA 1080p Dual Audio BDRip 10 bits DD x265-EMBER" / "S01E01-Rough Sketch [E6EA218B].mkv", ""),
        (test_root / "Another S01+OVA 1080p Dual Audio BDRip 10 bits DD x265-EMBER" / "S01E12-Stand by Oneself [2946B7EC].mkv", ""),
        (test_root / "Another S01+OVA 1080p Dual Audio BDRip 10 bits DD x265-EMBER" / "S01OVA-The Other [918CA797].mkv", ""),
        
        # Tenki no Ko
        (test_root / "[Beatrice-Raws] Tenki no Ko [BDRip 3840x2160 HEVC HDR DTSHD]" / "[Beatrice-Raws] Tenki no Ko [BDRip 3840x2160 HEVC HDR DTSHD].mkv", ""),
        (test_root / "[Beatrice-Raws] Tenki no Ko [BDRip 3840x2160 HEVC HDR DTSHD]" / "Audio 5.1" / "[Beatrice-Raws] Tenki no Ko [BDRip 3840x2160 HEVC HDR DTSHD]_Eng_Audio_5.1.mka", ""),
        (test_root / "[Beatrice-Raws] Tenki no Ko [BDRip 3840x2160 HEVC HDR DTSHD]" / "Audio Guide" / "[Beatrice-Raws] Tenki no Ko [BDRip 3840x2160 HEVC HDR DTSHD].Audio Guide.mka", ""),
        (test_root / "[Beatrice-Raws] Tenki no Ko [BDRip 3840x2160 HEVC HDR DTSHD]" / "BD menu" / "[Beatrice-Raws] Tenki no Ko (BD Menu) [BDRip 3840x2160 HEVC HDR E-AC3].mkv", ""),
        
        # Bungou Stray Dogs
        (test_root / "Bungou Stray Dogs" / "Bungou Stray Dogs" / "[DB]Bungou Stray Dogs_-_01_(Dual Audio_10bit_BD1080p_x265).mkv", ""),
        (test_root / "Bungou Stray Dogs" / "Bungou Stray Dogs" / "[DB]Bungou Stray Dogs_-_12_(Dual Audio_10bit_BD1080p_x265).mkv", ""),
        (test_root / "Bungou Stray Dogs" / "Bungou Stray Dogs" / "Extras" / "[DB]Bungou Stray Dogs_-_NCOP_(10bit_BD1080p_x265).mkv", ""),
        (test_root / "Bungou Stray Dogs" / "Bungou Stray Dogs Dead Apple" / "[DB]Bungou Stray Dogs Dead Apple_-_(Dual Audio_10bit_BD1080p_x265).mkv", ""),
        
        # Charlotte
        (test_root / "Charlotte [BD][1080p][HEVC 10bit x265][Dual Audio][Tenrai-Sensei]" / "Season 1" / "Charlotte (2015) - S01E01 - I Think About Others.mkv", ""),
        (test_root / "Charlotte [BD][1080p][HEVC 10bit x265][Dual Audio][Tenrai-Sensei]" / "Season 1" / "Charlotte (2015) - S01E13 - Memories To Come.mkv", ""),
        (test_root / "Charlotte [BD][1080p][HEVC 10bit x265][Dual Audio][Tenrai-Sensei]" / "Specials" / "Charlotte (2015) - S00E02 - The Strong Ones.mkv", ""),
        
        # THE IDOLM@STER Cinderella Girls
        (test_root / "[CookieSubs] THE IDOLM@STER Cinderella Girls [BD 1080p HEVC FLAC]" / "S1" / "[CookieSubs] THE IDOLM@STER Cinderella Girls - EP01 [BD 1080p HEVC FLAC].mkv", ""),
        (test_root / "[CookieSubs] THE IDOLM@STER Cinderella Girls [BD 1080p HEVC FLAC]" / "S1" / "[CookieSubs] THE IDOLM@STER Cinderella Girls - EP13 [BD 1080p HEVC FLAC].mkv", ""),
        (test_root / "[CookieSubs] THE IDOLM@STER Cinderella Girls [BD 1080p HEVC FLAC]" / "Special" / "[CookieSubs] THE IDOLM@STER Cinderella Girls - Anytime, Anywhere with Cinderella. [BD 1080p HEVC FLAC].mkv", ""),
        
        # Danganronpa
        (test_root / "Danganronpa Complete Package [Presented By EMBER]" / "01.Danganronpa The Animation S01 1080p Dual Audio BDRip 10 bits DD x265-EMBER" / "S01E01-Welcome to Despair High School [3D812AF5].mkv", ""),
        (test_root / "Danganronpa Complete Package [Presented By EMBER]" / "02.Danganronpa 3 Future Arc 1080p Dual Audio BDRip 10 bits DD x265-EMBER" / "S01E01-Third Time's the Charm [56BECC03].mkv", ""),
        (test_root / "Danganronpa Complete Package [Presented By EMBER]" / "04.Danganronpa 3 Hope Arc 1080p Dual Audio BDRip 10 bits DD x265-EMBER" / "S01E01-The School of Hope and the Students of Despair [1E6347F2].mkv", ""),
        
        # Hibike! Euphonium
        (test_root / "Hibike! Euphonium" / "Hibike! Euphonium" / "[DB]Hibike! Euphonium_-_01_(10bit_BD1080p_x265).mkv", ""),
        (test_root / "Hibike! Euphonium" / "Hibike! Euphonium" / "Extras" / "[DB]Hibike! Euphonium_-_NCED_(10bit_BD1080p_x265).mkv", ""),
        (test_root / "Hibike! Euphonium" / "Hibike! Euphonium Movies" / "[DB]Liz to Aoi Tori_-_(Dual Audio_10bit_BD1080p_x265).mkv", ""),
        
        # Girls Band Cry
        (test_root / "[Moozzi2] Girls Band Cry [ x265-10Bit Ver. ] - TV + SP" / "[Moozzi2] Girls Band Cry - 01 (BD 1920x1080 x265-10Bit FLACx2).mkv", ""),
        (test_root / "[Moozzi2] Girls Band Cry [ x265-10Bit Ver. ] - TV + SP" / "EXTRA" / "[SP13] BD Scans" / "[SP13] BD Scan - 01.rar", ""),
        
        # No Game No Life
        (test_root / "No Game No Life [BD][1080p][HEVC 10bit x265][Dual Audio][Tenrai-Sensei]" / "Season 1" / "No Game No Life - S01E01 - Beginner.mkv", ""),
        (test_root / "No Game No Life [BD][1080p][HEVC 10bit x265][Dual Audio][Tenrai-Sensei]" / "Other" / "No Game No Life - NCED - Oracion.mkv", ""),
        (test_root / "No Game No Life [BD][1080p][HEVC 10bit x265][Dual Audio][Tenrai-Sensei]" / "Specials" / "No Game No Life - S00E08 - No Game No Life Zero.mkv", ""),
        
        # Idoly Pride
        (test_root / "[Nyanpasu] Idoly Pride 1-12 Batch [v2][BD][1080p][HEVC][FLAC]" / "[Nyanpasu] Idoly Pride - 01 [1080p][HEVC][FLAC][BD][4E58E1CA].mkv", ""),
        (test_root / "[Nyanpasu] Idoly Pride 1-12 Batch [v2][BD][1080p][HEVC][FLAC]" / "EXTRAS" / "MENU" / "BD1.png", ""),
        
        # Melancholous Haruhi (funny word xd)
        (test_root / "[Sokudo] The Melancholy of Haruhi Suzumiya 2006+2009+Movie [1080p BD][AV1][dual audio]" / "2006" / "[Sokudo] The Melancholy of Haruhi Suzumiya 2006 - 01 [1080p BD][AV1][dual audio].mkv", ""),
        (test_root / "[Sokudo] The Melancholy of Haruhi Suzumiya 2006+2009+Movie [1080p BD][AV1][dual audio]" / "Movie" / "[Sokudo] The Disappearance of Haruhi Suzumiya (2010) [1080p BD][AV1][dual audio].mkv", ""),
        
        # Wonder Egg Priority
        (test_root / "Wonder Egg Priority (BDRip 1080p HEVC FLAC) [Dae]" / "[Dae] Wonder Egg Priority - S01E01 (BDRip 1080p HEVC FLAC) [Dual-Audio] [338A15C6].mkv", ""),
        (test_root / "Wonder Egg Priority (BDRip 1080p HEVC FLAC) [Dae]" / "Extras" / "NCs" / "[Dae] Wonder Egg Priority - NCED (BDRip 1080p HEVC FLAC) [72468D54].mkv", ""),
        (test_root / "Wonder Egg Priority (BDRip 1080p HEVC FLAC) [Dae]" / "Extras" / "Fonts" / "ACaslonPro-Bold.OTF", ""),
        
        # Zombie Land Saga test files for Season 1
        (test_root / "Zombie.Land.Saga.S01.v2.1080p.BluRay.10-Bit.Dual-Audio.FLAC5.1.x265-YURASUKA" / "Zombie.Land.Saga.S01E01.v2.1080p.BluRay.10-Bit.Dual-Audio.FLAC5.1.x265-YURASUKA.mkv", ""),
        (test_root / "Zombie.Land.Saga.S01.v2.1080p.BluRay.10-Bit.Dual-Audio.FLAC5.1.x265-YURASUKA" / "Zombie.Land.Saga.S01E12.v2.1080p.BluRay.10-Bit.Dual-Audio.FLAC5.1.x265-YURASUKA.mkv", ""),
        
        # Zombie Land Saga test files for Season 2
        (test_root / "Zombie.Land.Saga.S02.1080p.BluRay.10-Bit.Dual-Audio.FLAC5.1.x265-YURASUKA" / "Zombie.Land.Saga.S02E01.1080p.BluRay.10-Bit.Dual-Audio.FLAC5.1.x265-YURASUKA.mkv", ""),
        (test_root / "Zombie.Land.Saga.S02.1080p.BluRay.10-Bit.Dual-Audio.FLAC5.1.x265-YURASUKA" / "Zombie.Land.Saga.S02E12.1080p.BluRay.10-Bit.Dual-Audio.FLAC5.1.x265-YURASUKA.mkv", ""),
    ]
    
    for file_path, content in files:
        # Create empty file
        with open(file_path, 'w') as f:
            f.write(content)

def main():
    parser = argparse.ArgumentParser(description='Create test anime directory structure')
    parser.add_argument('dir', nargs='?', default='./anime_test', help='Directory to create test files in')
    
    args = parser.parse_args()
    
    os.makedirs(args.dir, exist_ok=True)
    create_test_structure(args.dir)
    
    print(f"Test anime files and folders created in: {os.path.abspath(args.dir)}")
    print("Run decancer.py on this directory to see how files would be renamed.")

if __name__ == "__main__":
    main()
