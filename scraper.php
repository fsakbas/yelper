<?php

# Blank PHP
$url = "http://www.yelp.com/search?find_desc=gym&find_loc=Richmond+Hill%2C+ON&ns=1#l=p:ON:Toronto::%5BAlexandra_Park,Bayview_Village,Beaconsfield_Village,Bickford_Park,Bloor-West_Village,Bloordale_Village,Brockton_Village,Cabbagetown,Casa_Loma,Chinatown,Christie_Pits,Church-Wellesley_Village,City_Place,Corktown,Corso_Italia,Deer_Park,Discovery_District,Distillery_District,Dovercourt,Downsview,Downtown_Core,Dufferin_Grove,East_York,Entertainment_District,Etobicoke,Financial_District,Greektown,Harbourfront,High_Park,Hogg's_Hollow,Kensington_Market,Koreatown,Lawrence_Park,Leslieville,Liberty_Village,Little_Italy,Little_Portugal,Moore_Park,Mount_Pleasant_and_Davisville,New_Toronto,Niagara,Ossington_Strip,Palmerston,Parkdale,Queen_Street_West,Rexdale,Riverdale,Roncesvalles,Rosedale,Ryerson,Scarborough,Seaton_Village,South_Hill,St._Lawrence,Summer_Hill,Swansea,The_Annex,The_Beach,The_Danforth,The_Junction,Trinity_Bellwoods,University_of_Toronto,Upper_Beach,Wallace_Emerson,West_Don_Lands,West_Queen_West,Willowdale,Wychwood,Yonge_and_Eglinton,Yonge_and_St._Clair,Yorkville%5D";
$html = scraperWiki::scrape($url);

require 'scraperwiki/simple_html_dom.php';
$dom = new simple_html_dom();
$dom->load($html);
foreach($dom->find(".businessresult") as $data){
    $img = $data->find(".photo-img");
    print $img[0]->plaintext;
}

?>
