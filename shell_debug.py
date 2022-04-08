from scrapy import cmdline

spider = 'spider_name_here'
arguments = [
    # '-a name=value',
]

command = f'scrapy crawl {spider}'
if arguments:
    arguments = " ".join(arguments)
    command = f'{command} {arguments}'

cmdline.execute(command.split())
