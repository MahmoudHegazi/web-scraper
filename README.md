# web-scraper
https://www.edureka.co/blog/web-scraping-with-python/
https://stackoverflow.com/questions/59130672/how-to-scrape-pdfs-using-python-specific-content-only

https://www.google.com/robots.txt
http://www.robotstxt.org/robotstxt.html

https://librarycarpentry.org/lc-webscraping/setup

#task one 
scrap this one, update changes with ajax if not updated

# selenum by
```python
 Set of supported locator strategies.\n    ', 'ID': 'id', 'XPATH': 'xpath', 'LINK_TEXT': 'link text', 'PARTIAL_LINK_TEXT': 'partial link text', 'NAME': 'name', 'TAG_NAME': 'tag name', 'CLASS_NAME': 'class name', 'CSS_SELECTOR': 'css selector', '__dict__': <attribute '__dict__' of 'By' objects>, '__weakref__': <attribute '__weakref
 
 ```
# get any element contains text js
```javascript
const getElementByText = (text, possibleElms=['div', 'span', 'h5', 'h4', 'button', 'p','h6'])=>{
    const elementsToSearch = [];
    const resultElements = [];
    possibleElms.forEach( (elmType)=>{
        const SearchElements = document.querySelectorAll(elmType);
        if (SearchElements.length){
          SearchElements.forEach( (SearchElement)=>{
           if (!elementsToSearch.includes(SearchElement)){
              elementsToSearch.push(SearchElement);
            }
          })
        }
    });
    console.log(elementsToSearch);
    const searchText = text.toLowerCase().trim();
    
    elementsToSearch.forEach( (elm)=>{
        const ElmTxt = elm.innerText.toLowerCase().trim();
        if (ElmTxt == searchText){
            if (!resultElements.includes(ElmTxt)){
                resultElements.push(elm);
            }
        }
        
    });
    return resultElements;
    
}
undefined
let maybe = getElementByText('Sign in');

```
# PHP
https://simplehtmldom.sourceforge.io/


# create new local copy from web page html content text into your pc using  curl
 ```curl -o curl_test.txt https://www.google.com```
 
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
https://lightsail.aws.amazon.com/ls/docs/en_us/articles/migrate-your-wordpress-blog-to-amazon-lightsail


https://selenium-python.readthedocs.io/api.html


### scroller robot js



```
const x = ()=> {
setTimeout(function(){
document.body.style.height = '2000px';
}, 3000);
}

const n = ()=> {
setTimeout(function(){
console.log(document.body.scrollHeight);
window.scrollTo(0, document.body.scrollHeight);
}, 4000);


}
x();
n();

```
### to excute js in python with selnuim 
 driver.execute_script
 
 
### dynamic error handle

```
proxy_list = ['1','2','3','4','5','6']
erro_counter = 0
proxy = ''
proxys = []
mbool = True
while mbool:
    try:
        proxy = proxy_list[erro_counter]
        print(proxys[0])
        print(proxy)
        mbool = False
    except IndexError:
        erro_counter += 1
        proxy = proxy_list[erro_counter]
        proxys.append('handling')
        print('error')
        mbool = True
```


### js Mouseover Action

```
var element = document.querySelector('.top-nav-item.wt-pb-xs-2.wt-mr-xs-2.wt-display-flex-xs.wt-align-items-center');
element.addEventListener('mouseover', function() {
  console.log('Event triggered');
});

var event = new MouseEvent('mouseover', {
  'view': window,
  'bubbles': true,
  'cancelable': true
});

```

## new split for numbers
```
priceString = "Rs249.5"

def advancedSplit(unformatedtext):
    custom_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    priceList = []
    str_length = len(unformatedtext)
    index = 0
    for l in range(len(unformatedtext)):
        if unformatedtext[l] in custom_numbers:
            price = unformatedtext[slice(l, len(unformatedtext))]
            currency = unformatedtext[slice(0,l)]
            if currency == "Rs" or currency == "RS":
                currency = "INR"
             
            priceList.append(price)
            break
        elif index == str_length:
            priceList.append("")
            priceList.append("unformatedtext")
            break
        else:
            continue
            
        index += 1
    return priceList
print(advancedSplit(priceString))
```
