% rebase('osnova.tpl')


<h1>Vnesite potenco:</h1>
<form action="/shrani-potenco/" method="POST" class="matrika">
	<div class="vrstica">
		<input type="number" step="any" class="element" name="potenca" autofocus required>
	</div>
	<input type="submit" value="Shrani potenco" class="matrika">
</form>
