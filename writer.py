import scrape


def write_script(name, season_no, episode_number, script, directory):
    # if directory[len(directory)-1]!= '\\':
        # pass
    file_name = directory + name + "-s" + scrape.number_to_str(season_no) + "e" + scrape.number_to_str(episode_number) + ".txt"
    f = open(file_name, 'w', encoding="utf-8")
    f.write(script)
    return True
