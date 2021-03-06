from time import clock

from source.train_schedule import Schedule


def search_db():
    """
    search record in database, which path input from stdin
    :return: 0 
    """
    database = input('Input database name: ')
    show = input('Show suitable records?(Y/N default -- Yes): ')
    if show.lower() == 'n':
        show = False
    elif show.lower() == 'y':
        show = True
    print('LOADING DATABASE...')
    schedule = Schedule(database)
    schedule.load_database()
    print('CREATING DICT...')
    schedule.convert_to_dict()
    print('CREATING SIMPLE HASH TABLE...')
    schedule.convert_to_simple_hash_table()
    print('CREATING RS HASH TABLE...')
    schedule.convert_to_rs_hash_table()
    while True:
        type = input('Type of search(linear/binary(work only on sorted database)/map/simple/rs): ')
        time = input('Type searching time (format MM-DD HH:MM): ')
        if type == 'linear':
            start = clock()
            schedule.linear_search(time, show=show)
            print('Time of search %s' % (clock() - start))
        elif type == 'binary':
            start = clock()
            schedule.binary_search(time, show=show)
            print('Time of sorting %s' % (clock() - start))
        elif type == 'map':
            start = clock()
            schedule.map_search(time, show=show)
            print('Time of sorting %s' % (clock() - start))
        elif type == 'simple':
            start = clock()
            schedule.simple_hash_search(time, show=show)
            print('Time of sorting %s' % (clock() - start))
        elif type == 'rs':
            start = clock()
            schedule.rs_hash_search(time, show=show)
            print('Time of sorting %s' % (clock() - start))
        else:
            print('Unknown Search!')
        test = input('Type "C" and Enter to search by new time or just Enter to exit: ')
        if test.lower() != 'c':
            break
    return 0

if __name__ == "__main__":
    search_db()
