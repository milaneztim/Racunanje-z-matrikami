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
			width: 4.5em;
			margin: 0.5em;
		}
	</style>
</head>
<body>	
	<h2>Rezultat:</h2>
	<div class="matrika">
		% for i in range(m):
			<div class="vrstica">
				% for j in range(n):
					<input type="number" step="any" class="element" name="{{i}}x{{j}}" value="{{rezultat[i][j]}}">
				% end
			</div>
		% end
	</div>
	<form action="/dodaj-matriko/A" method="POST" class="matrika">
	<input type="submit" value="Uporabi to matriko">
	</form>
	<form action="/vnos-dimenzije/A" method="POST" class="matrika">
	<input type="submit" value="Nov račun">
	</form>
</body>
</html>