<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Matrike</title>

	<style>
	
		.matrika {
			margin: 1em;
		}

		.vrstica {
			display: flex;
			flex-direction: row;
			justify-content: center;
			align-items: center;
			width: fit-content;
		}

		.element {
			width: 3em;
			margin: 0.5em;
		}
	</style>
</head>
<body>
	<h2>Rezultat:</h2>
	<p>
		% for _ in range(2):
			{{rezultat}}
		% end
		% for _ in range(2):
			{{test}}
		% end
	</p>
</body>
</html>