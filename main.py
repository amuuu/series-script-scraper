import sys, scrape

# name, season_from=NUMBER, season_to=NUMBER, saving_dir
scrape.Scraper().scrape(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
