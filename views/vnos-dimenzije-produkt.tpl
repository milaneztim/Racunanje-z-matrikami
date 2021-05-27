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
	<div class="">
		<h2>Vnesite dimenzijo:</h2>
		<form action="/vnos-matrike/B" method="POST" class="matrika">
			<div class="vrstica">
				<input type="number" class="element" name="m" value="{{m}}" readonly>
				<input type="number" step="any" min="1" max="10" class="element" name="n" required>
			</div>
			<input type="submit" value="Shrani dimenzijo">
		</form>
	</div>
</body>
</html>