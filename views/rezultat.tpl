!DOCTYPE html>
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
	<div class="">
		<h2>Vnesite elemente matrike</h2>
		<form action="/dodaj-matriko/{{ime_matrike}}" method="POST" class="matrika">
			% for i in range(m):
				<div class="vrstica">
					% for j in range(n):
						<input type="number" step="any" class="element" placeholder="0" name="{{i}}x{{j}}">
					% end
				</div>
			% end
			<input type="submit" value="Shrani matriko">
		</form>
	</div>
</body>
</html>