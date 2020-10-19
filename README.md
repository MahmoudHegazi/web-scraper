# web-scraper
https://www.edureka.co/blog/web-scraping-with-python/



# PHP
https://simplehtmldom.sourceforge.io/


#first version scrap google image, and title
<img src='top_scrap.PNG'>


```
<?php
require 'simple_html_dom.php';

$html = file_get_html('http://www.google.com/');
$title = $html->find('a', 1); // any tag get it awesome
$image = $html->find('img', 0);
$div = $html->find('div', 0);

echo $title->plaintext."<br>\n";
echo '<img src="https://www.google.com'.$image->src .'">';
echo $div;
?>
```






https://www.google.com/search?rlz=1C1PNBB_enEG898EG899&sxsrf=ALeKk02jA9-eqSFqsojXNpM8plWWECMUUw%3A1602797275666&ei=276IX-OTKMuelwSK6JPIDw&q=can+i+scrape+through+google+search+results&oq=can+I+scrap+throgh+google+sea&gs_lcp=CgZwc3ktYWIQAxgAMgoIIRAWEAoQHRAeMgoIIRAWEAoQHRAeOgQIABBHOgQIIxAnOgcILhDJAxBDOgQILhBDOgUIABCRAjoFCAAQsQM6CwguELEDEMcBEKMCOggILhDJAxCRAjoCCC46CAguELEDEIMBOgIIADoKCC4QsQMQyQMQQzoICC4QsQMQkQI6DQguELEDEMcBEKMCEEM6BAgAEEM6BQguELEDOgUIABDJAzoECC4QCjoGCAAQFhAeOggIABAWEAoQHjoHCAAQyQMQDToECAAQDToJCAAQyQMQFhAeOgQIIRAKOgcIIRAKEKABUMo0WMN2YLJ9aAJwBHgAgAG9AYgBoCCSAQQwLjMxmAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab



https://blog.apify.com/unofficial-google-search-api-from-apify-22a20537a951

```python
from io import StringIO
from email.generator import Generator
fp = StringIO()
g = Generator(fp, mangle_from_=True, maxheaderlen=60)
g.flatten(msg)
text = fp.getvalue()
从Python 3.0开始，StringIO和cStringIO模块已经取消。通过import io模块代替，分别使用io.String或io.BytesIO处理文本和数据。从Python 3邮件流文档能看到相关实现StringIO的代码为：

from io import StringIO
from email.generator import Generator
fp = StringIO()
g = Generator(fp, mangle_from_=True, maxheaderlen=60)
g.flatten(msg)
text = fp.getvalue()
```
```
0

I like the Dom Crawler library. Very easy to use, has lots of options like:

$crawler = $crawler
->filter('body > p')
->reduce(function (Crawler $node, $i) {
    // filters every other node
    return ($i % 2) == 0;
});
```
