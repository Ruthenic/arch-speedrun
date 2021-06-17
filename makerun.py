import os,json,shutil
defaultindex = open("index.html").read()
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
	getFooter("runfooter.html")
    </script>
    <h2>{0} by {1}</h2>
    <iframe width="560" height="315" src="{2}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    <p>Commands used:</p>
    <pre>{3}</pre>
    <p>Runner's comment: {4}</p>
	<div id="footer">
	</div>
</body>
</html>
"""
runs = []
for run in os.listdir("../runs"):
    tmp = run
    run = json.load(open("../runs/" + run))
    runs.append({"Runner": run["runner"], "Time": run["time"], "Commands": run["commands"], "Video": run["video"], "Comment": run["comment"], "HTML Name": tmp})
runs = sorted(runs, key=lambda k: k['Time'])
indexed = ""
for run in runs:
    runner = run["Runner"]
    time = run["Time"]
    commands = ""
    for i in run["Commands"]:
        commands += i + "\n"
    video = run["Video"]
    comment = run["Comment"]
    newhtml = ".".join(run["HTML Name"].split(".")[:-1]) + ".html"
    with open(newhtml, "w") as f:
        f.write(default.format(time, runner, video, commands, comment))
    with open(newhtml) as f:
        print(f.read())
    indexed += "<a href = '{0}'>{1} - {2}</a><br>\n    ".format(newhtml, time, runner)
index = defaultindex.replace("{runs}", indexed)
print(index)
with open("index.html", "w") as f:
    f.write(index)
