
function do_dl(){
	function wait(ms){
		var start = new Date().getTime();
		var end = start;
		while(end < start + ms) {
			end = new Date().getTime();
		}
	}
	function downloadURI(uri, name) 
	{
		var link = document.createElement("a");
		link.download = name;
		link.href = uri;
		wait(15000);
		link.click();
		
	}

	var i;
	var yrs = [];
	var months=["January","February","March","April","May","June","July","August","September","October","November","December"];
	for (i = 2001; i < 2002; i++) { 
	yrs.push(i);
	}

	for (yr in yrs){
		for (month in months)
		{
		k = yrs[yr]+"/"+months[month]+yrs[yr]+"ChiefsDirectory.pdf";
		l = months[month]+yrs[yr]+"ChiefsDirectory.pdf";
		uri = "https://www.cia.gov/library/publications/resources/world-leaders-1/pdfs/"+k;
		downloadURI(uri,l);
		console.log(uri);
		//setTimeout(downloadURI,3000)
		}
	}
}
function open_url()
{
	window.open("https://www.cia.gov/library/publications/resources/world-leaders-1/");
	do_dl();
}
