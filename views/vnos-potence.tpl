% rebase('osnova.tpl')


<h2>Vnesite potenco:</h2>
<form action="/shrani-potenco/" method="POST" class="matrika">
	<div class="vrstica">
		<input type="number" step="any" class="element" name="potenca" autofocus required>
	</div>
	<input type="submit" value="Shrani potenco" class="matrika">
</form>
