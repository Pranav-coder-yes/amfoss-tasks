const terminalOutput = document.querySelector('.terminal-output');
const terminalInput = document.querySelector('input[type="text"]');

function checkInput(event) {
    if (event.key === 'Enter') {
        const command = terminalInput.value.trim();
        handleInput(command);
    }
}

function handleInput(command) {
    switch (command.toLowerCase()) {
        case 'help':
            viewCommand();
            break;

        case 'fetch':
            fetchProducts();
            break;

        case 'clear':
            clearTerminal();
            break;

        default:
            terminalOutput.innerHTML += `Invalid command: ${command}\n`;
            break;
    }

    terminalInput.value = ''; // Clear input after the command
    terminalOutput.scrollTop = terminalOutput.scrollHeight; // Auto scroll
}

// View available commands
function viewCommand() {
    terminalOutput.innerHTML += "Available Commands: help, fetch, clear\n";
}

// Fetch products from FakeStoreAPI and display them in the terminal
function fetchProducts() {
    terminalOutput.innerHTML += "Fetching products...\n";

    fetch('https://fakestoreapi.com/products')
        .then(response => response.json())
        .then(products => {
            terminalOutput.innerHTML += "Products fetched:\n";
            products.forEach(product => {
                terminalOutput.innerHTML += `Product: ${product.title}, Price: $${product.price}\n`;
            });
        })
        .catch(error => {
            terminalOutput.innerHTML += `Error fetching products: ${error}\n`;
        });
}

// Clear the terminal output
function clearTerminal() {
    terminalOutput.innerHTML = '';
}
