% rebase('osnova.tpl')



<h1>Vnesite dimenzijo:</h1>
<form action="/vnos-matrike/B" method="POST" class="matrika">
	<div class="vrstica">
		<input type="number" class="element" name="m" value="{{m}}" readonly>
		<input type="number" step="any" min="1" max="10" class="element" name="n" autofocus required>
	</div>
	<input type="submit" value="Shrani dimenzijo">
</form>
