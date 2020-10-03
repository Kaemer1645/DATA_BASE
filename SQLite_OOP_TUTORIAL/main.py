from commands import cli, setup, add, category_list, category
from sys import argv
from dotenv import load_dotenv
load_dotenv()


cli.add_command(setup)
cli.add_command(add)
cli.add_command(category_list)
cli.add_command(category)


if __name__=='__main__':
    cli()



"""
if len(argv) == 2 and  argv[1] == 'setup':
    '''
        Initialize DataBase
        Usage: python main.py setup
    '''
    setup()

if len(argv) == 4 and argv[1] == 'add':
    '''
    Adding new variable
    Usage: python main.py add --category-- http://google.com
    '''
    add(category=argv[2], url=argv[3])

if len(argv) == 3 and argv[1] == 'category':
    '''
    Search data by category
    Usage: python main.py catergory --category name--
    '''
    category(category_name=argv[2])

if len(argv) == 2 and argv[1] == 'category_list':
    '''
    Display list of added categories
    '''
    category_list()


"""

