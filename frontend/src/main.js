import './style.css'
import javascriptLogo from './javascript.svg'
import viteLogo from '/vite.svg'
import { setupCounter } from './counter.js'



document.querySelector('#app').innerHTML = `
  <div>
    <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
      <img src="${javascriptLogo}" class="logo vanilla" alt="JavaScript logo" />
    </a>
    <h1>MoodText</h1>
    <div class="card">
<form action="/action_page.php">
  <input type="file" id="myFile" name="filename">
  <input type="submit">
</form>
    </div>
    <div class="dropdown">
  <button class="dropbtn">Dropdown</button>
  <div class="dropdown-content">
  <a href="#">Link 1</a>
  <a href="#">Link 2</a>
  <a href="#">Link 3</a>
  </div>
  </div>
  <div>
    <h1>Ask me a question</h1>
  <input type="text" id="user-input">
  <button id="fetch-data">Submit</button>
  <pre id="result"></pre>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script type="module">
    // Function to make the OpenAI API request
    async function fetchCompletion(userMessage) {
      const apiKey = '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';
      const url = 'https://api.openai.com/v1/chat/completions';
      const headers = {
        'Authorization': 'Bearer ${apiKey}',
        'Content-Type': 'application/json'
      };
      const data = {
        model: 'gpt-3.5-turbo',
        messages: [
          { role: 'system', content: 'You are a helpful assistant.' },
          { role: 'user', content: userMessage }
        ]
      };

      try {
        const response = await axios.post(url, data, { headers });
        console.log(response.data)
        const result = response.data.choices[0].message.content;
        resultElement.textContent = result;
      } catch (error) {
        console.error("Error fetching data:", error);
        resultElement.textContent = "Error fetching data. Check console for details.";
      }
    }

    // DOM elements
    const userInputElement = document.getElementById('user-input');
    const fetchDataButton = document.getElementById('fetch-data');
    const resultElement = document.getElementById('result');

    // Event listener
    fetchDataButton.addEventListener('click', () => {
      const userInput = userInputElement.value;
      fetchCompletion(userInput);
    });
  </div>
  
  </div>
  
`

setupCounter(document.querySelector('#counter'))
