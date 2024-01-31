<script>
	// Images
	import reload_img from "$lib/imgs/reload_keys_symbol.png"
	import logo_img from "$lib/imgs/winton.jpg"
	import crown_img from "$lib/imgs/leaderboard_img.png"

	//structure
	import Word_blocks from './word_boxes.svelte'


	//app functionality/code blocks
	const num_lines = 10000
    const num_blocks = 25; // Define the number of blocks you want to create

    // import main_words from "$lib/words/top1kwords.txt"
</script>

<svelte:head>
	<title> Typing Site</title>
</svelte:head>
<!-- header -->
<h1>
	<img src={logo_img} alt = "wynton"
	width = 35/>
	TypingTest
	<span>
		<button>
			<img src={reload_img} alt="reload img"
			width = 30/>
		</button>
		<!-- <button>
			<img src={crown_img} alt="button for leaderboards" />
			height: 10%;
			width:10%;
		
		</button> -->
	</span>
	
</h1>


<Word_blocks />

<style>
	/* .box{
        display:flex;
        font: 'Gotham';
        color: rgb(139, 59, 59);
        font-size: 100;
        font-weight: 70;
    } */

	h1{
		color: rgb(139, 59, 59);
		font-family: 'Gotham';
		font-size: 1.75em;
		font-weight: 600;
	}

	:global(body) { 
		background-color: rgb(41, 35, 36);
  }

</style>
