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

        .button {
            border: solid;
            padding: 10px 15px;
            margin: 7px 7px;
            font-size: 16px
        }

        table {
            font-family: arial, sans-serif;
            border-collapse: collapse;
            width: 100%;
        }
	</style>
</head>
<body>
	<div class="">
		<h2>Izberi operacijo</h2>
            <table>
                <form action="/vnos-dimenzije/B" method="POST" class="matrika">
                    <tr>
                        <th><input type="image" src="/../img/plus.png" alt="+" class="button" name="plus";></th>
                        <th><input type="image" src="/../img/minus.png" alt="-" class="button" name="minus";></th>                
                        <th><input type="image" src="/../img/produkt.png" alt="*" class="button" name="produkt";></th>
                    </tr>    
                    <tr>
                        <th><input type="image" src="/../img/hadamard.png" alt="o" class="button" name="hadamard";></th>
                        <th><input type="image" src="/../img/up-arrow.png" alt="^" class="button" name="potenca";></th> 
                </form>
                <form action="/rezultat/" method="POST" class="matrika">               
                        <th><input type="image" src="/../img/det1.jpg" alt="det" class="button" name="det";></th>
                    </tr>
                    <tr>
                        <th><input type="image" src="/../img/trace.jpg" alt="t" class="button" name="trace"></th>
                        <th><input type="image" src="/../img/transpose.png" alt="tr" class="button" name="transpose";></th>            
                    </tr>
                </form> 
		</form>
	</div>
    <img src="/..img/plus.png" alt="+">
</body>
</html>