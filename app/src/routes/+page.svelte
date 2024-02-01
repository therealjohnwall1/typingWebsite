<script>
	// Images
	import reload_img from "$lib/imgs/reset.png"
	import logo_img from "$lib/imgs/winton.jpg"
	import crown_img from "$lib/imgs/leaderboard_img.png"
	
	import Word_body from './word_body.svelte'
	
	import { onMount } from 'svelte';
      // globs
    let WORD_AMT = 25;
    const back_domain = "http://localhost:8000";
    $: word_bank = [];

    console.log("innitalizing word bank");

    onMount(async () => {
        console.log(`Mounting dom`)
        console.log(WORD_AMT)
        word_bank = get_words(WORD_AMT)
		console.log("type: " + typeof word_bank);
		console.log("bank: " + word_bank);
    });

    function handle_keypress(event){
        pass
    }

    async function get_words(){
        const params = {
            size: WORD_AMT
        };

        const queryString = Object.keys(params)
        .map(key => encodeURIComponent(key) + '=' + encodeURIComponent(params[key]))
        .join('&');
       
        const url = `${back_domain}/getWords?${queryString}`;

        await fetch(url)
            .then(response => {
            if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
            }
            return response.json();
            })
            .then(data => {
			word_bank = data;
            console.log("works: " + data);
            })
            .catch(error => {
            console.error('Error:', error);
            });
    }

	
	function changeWords15(){
		WORD_AMT = 15;
	}
	function changeWords25(){
		WORD_AMT = 25;
	}
	function changeWords50(){
		WORD_AMT = 50
	}
	function changeWords100(){
		WORD_AMT = 100
	}
	function customWords(){
		pass
	}

	let count = 1;

	console.log("check");
	console.log("bank2: " + word_bank);

</script>

<svelte:head>
	<title> Typing Site</title>
</svelte:head>

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


<div>
	{#each word_bank as word}
		{#each word as letter}
		<letter> {letter} </letter>
		{/each}
	{/each}
</div>



<style>
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
