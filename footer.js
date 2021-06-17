async function getFooter(footerPath) {
	if (footerPath === undefined) {
		//why the hell does js not have optional parameters for functions? 
		footerPath = "/footer.html";
	}
	console.log("sanity check much?");
	console.log(footerPath)
	footer = await fetch(footerPath);
	footer = await footer.text();
	document.getElementById("footer").innerHTML = footer;
}
