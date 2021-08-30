from scrapy import cmdline

spider = 'spider_name_here'
arguments = [
    # 'name=value',
]

command = f'scrapy crawl {spider}'
if arguments:
    arguments = " -a ".join(arguments)
    # -a will not be present for for first argument
    command = f'{command} -a {arguments}'

cmdline.execute(command.split())
