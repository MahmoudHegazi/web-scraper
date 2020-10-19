<?php
require 'simple_html_dom.php';
$udacity_url = file_get_html('https://egypt.souq.com/eg-en/');
$home_url = 'https://www.freelancer.com/';
$google_url = file_get_html('https://www.google.com/');
$html = file_get_html('https://macdiscussions.udacity.com/');
$html1 = file_get_html('https://www.freelancer.com/dashboard');
$title = $html->find('title', 0);
$title1 = $html1->find('title', 0);
$image_google = $google_url->find('img', 0);
$image = $html1->find('img', 0);
$udacity_image = $udacity_url->find('img', 0);
echo $title->plaintext;
echo $title1->plaintext;
echo $image->src;
#echo $title->href . "<br>\n";
#echo '<a href="' . $home_url .$title->href . '">' . "I'm Top</a>"; 
#echo $title->plaintext."<br>\n";
echo '<br><br><br><br><hr><h2>Web Scrap SOUQ Image<h2><img src="'.$udacity_image->src .'">';
echo '<br><br><br><br><hr><h2>Web Scrap FreeLancer Image<h2><img src="'.$image->src .'">';
echo '<br><br><br><br><hr><h2>Web Scrap Google Image<h2><img src="https://www.google.com'.$image_google->src .'">';
?>
