# scrapy_debug_helper
A script you can add into a scrapy project to help access debuggers during spider runs.

## Set up

Simply add the script into this part of your scrapy project

```
project_name
│   shell_debug.py <--------   
│   scrapy.cfg  
└───crawler_name
│   |   items.py
│   |   settings.py  
│   └───spiders
│       │   spider_name.py
...
```

## Using

1. In `shell_debug.py` update line 3 with the name of the spider you want to run.    
2. (optional) add any additional arguments for the spider to the arguments list on line 4
3. In spider_name.py add breakpoints where needed.
4. Run shell_debug.py in debug mode.

## Pros and Cons
### Advantages over standard scrapy shell
- For more advanced IDEs will utilise code completion, etc from a native python console.
- It will have imported any relevant functions at the time the console opens.
- Any initial set ups like location setting, login, etc could be completed by the spider prior to hitting the breakpoint.

### Disadvantages over standard scrapy shell
- Requires adding additional code to the spider if specific urls should be obtained. 
- Doesn't easily allow fetching a new url in the same session - have to exit, update relevant code to visit a new url and then restart.

## Tips

Override `start_requests` in your spiders with code that checks for arguments that can be used to send a specific url to be handled at a specific method. This can allow you to bypass full crawls quickly to test handling of specific pages.
