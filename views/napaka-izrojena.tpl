<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta value="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.css">
	<title>Matrike</title>
	<style>
		.matrika {
			margin: 1em;
		}
    </style>
</head>

<body>
    <h2>Pozor:</h2>
    <div style="margin:1em">
        Izbrana matrika je izrojena!
    </div>
    <form action="/vnos-dimenzije/A" method="POST" class="matrika">
        <input type="submit" value="Poskusi znova">
    </form>
</body>
</html> 
