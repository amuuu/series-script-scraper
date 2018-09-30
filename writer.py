import scrape


def write_script(name, season_no, episode_number, script, directory='./'):
    file_name = directory + name + "s" + scrape.number_to_str(season_no) + "e" + scrape.number_to_str(episode_number)
    f = open(file_name, 'w')
    f.write(script)
    return True
