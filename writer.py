def write_script(name, season_no, episode_number, script, directory='./'):
    file_name = directory + name + "s" + season_no + "e" + episode_number
    f = open(file_name, 'w')
    f.write(script)
    return True
