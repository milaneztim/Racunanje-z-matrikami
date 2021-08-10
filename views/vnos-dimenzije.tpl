% rebase('osnova.tpl')

<h1>Vnesite dimenzijo:</h1>
<form action="/vnos-matrike/{{ime_matrike}}" method="POST" class="matrika">
	<div class="vrstica">
		<input type="number" step="any" min="1" max="10" class="element" name="m" autofocus required>
		<input type="number" step="any" min="1" max="10" class="element" name="n" required>
	</div>
	<input type="submit" value="Shrani dimenzijo" class="matrika">
</form>
