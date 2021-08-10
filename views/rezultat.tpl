% rebase('osnova.tpl')


<h1>Rezultat:</h1>  
<div class="matrika">
<form action="/dodaj-matriko/A" method="POST" class="matrika">
	% for i in range(m):
		<div class="vrstica">
			% for j in range(n):
				<input type="number" step="any" class="element" name="{{i}}x{{j}}" value="{{rezultat[i][j]}}">
			% end
		</div>
	% end
<input type="submit" value="Uporabi to matriko">
</form>
</div>

<form action="/vnos-dimenzije/A" method="POST" class="matrika">
<input type="submit" value="Nov račun">
</form>
