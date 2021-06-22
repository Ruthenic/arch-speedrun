import os,json,shutil
defaultindex = open("index.html").read()
defaultcatpage = open("categorypage.html").read()
defaultrunfooter = open("runfooter.html").read()
os.chdir("content")
default = """<!DOCTYPE HTML>
<html lang="en">
<head>
    <title>{0} by {1}</title>
    <link rel="stylesheet" type="text/css" href="/css/dark-mode.css">
    <script src="/footer.js"></script>
</head>
<body>
    <script>
	getFooter("{6}footer.html")
    </script>
    <h2>{0} by {1}</h2>
    <iframe width="560" height="315" src="{2}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    <p>Commands used:</p>
    <pre>{3}</pre>
    <p>Runner's comment: {4}</p>
    <p>ISO version: {5}</p>
    <div style="position:relative;margin-bottom:105px;"></div> <!-- Add spacing so the comment doesn't get devoured by the footer -->
	<div id="footer">
	</div>
</body>
</html>
"""
runs = []
for run in os.listdir("../runs"):
    tmp = run
    run = json.load(open("../runs/" + run))
    runs.append({"Runner": run["runner"], "Time": run["time"], "Commands": run["commands"], "Video": run["video"], "Comment": run["comment"], "ISO": run["iso"], "HTML Name": tmp, "Category": run["category"]})
runs = sorted(runs, key=lambda k: k['Time'])
indexed = {}
for run in runs:
    runner = run["Runner"]
    time = run["Time"]
    commands = ""
    for i in run["Commands"]:
        commands += i + "\n"
    video = run["Video"]
    comment = run["Comment"]
    iso = run["ISO"]
    category = run["Category"]
    newhtml = ".".join(run["HTML Name"].split(".")[:-1]) + ".html"
    try:
        bige = open(category + newhtml)
    except:
        os.makedirs(category, exist_ok=True)
    with open(category + "/" + newhtml, "w") as f:
        f.write(default.format(time, runner, video, commands, comment, iso, "../" + category))
    with open(category + "/" + newhtml) as f:
        print(f.read())
    try:
        print(indexed[category])
    except:
        indexed[category] = ""
    indexed[category] += "<a href = '{0}'>{1} - {2}</a><br>\n    ".format(category + "/" + newhtml, time, runner)
#we don't actually modify the index anymore, but i don't feel like removing it rn because the script relies on it
#print(index)
cats = ""
for category, runs in indexed.items():
    catpage = defaultcatpage.replace("{runs}", runs).replace("{category}", category + "%")
    with open(category + ".html", "w") as f:
        f.write(catpage)
    runfooter = defaultrunfooter.replace("{catpage}", "../" + category + ".html").replace("{category}", category)
    with open(category + "footer.html", "w") as f:
        f.write(runfooter)
    cats += "<a href = '{0}'>{1}</a><br>\n    ".format(category + ".html", category + "%")
index = defaultindex.replace("{runs}", cats)
with open("index.html", "w") as f:
    f.write(index)
