from main import crawl

c = crawl('https://bs.to/serie/Boku-no-Hero-Academia-My-Hero-Academia')
c.session = 3
c.gui = "on"
c.get_serie()