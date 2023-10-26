function waitingDialog() {
    let waitingDialog = bootbox.dialog({
        message: '<p class="text-center mb-0"><i class="fas fa-spin fa-cog"></i> Please wait while we do something...</p>',
        closeButton: false
    });
    return waitingDialog;
}
function handleHistoryMessageElement(dataList) {
    let oldMessageDiv = document.getElementById('oldMessageDiv')
    oldMessageDiv.innerHTML = '';
    for (let i = 0; i < data.length ; i++) {
        let itemDiv = document.createElement('div')
        let messageDiv = document.createElement('div')
        let message = document.createTextNode(data[i]['board_message'])
        messageDiv.appendChild(message)

        let imageDiv = document.createElement('div')
        let imgElement = document.createElement('img')
        imgElement.classList.add('old-message-img')
        imgElement.src = data[i]['board_image_url']
        imageDiv.appendChild(imgElement)

        let hrElement = document.createElement('hr')
        hrElement.classList.add('hr-style')

        itemDiv.appendChild(messageDiv)
        itemDiv.appendChild(imageDiv)
        itemDiv.appendChild(hrElement)
        oldMessageDiv.appendChild(itemDiv)

    }
    
}

function queryAllHistoryMessage() {
    fetch('/rest/queryAllHistoryMessage').then((response) => {
        let result = response.json()
        if (response.status == 200) {
            return result
        }
        return null
    }).then((result) => {
        if (result) {
            data = result['data']
            console.log(data)
            handleHistoryMessageElement(data);
        }
    }).catch((error) => {
        console.log(error)
    });     
}
function initSubmitBtn() {
    document.getElementById('submitBtn').addEventListener('click', function() {
        
        let formData = new FormData(document.getElementById('formData'))
        let dialog = waitingDialog()
        fetch('/rest/uploadFile', {
            method: 'POST',
            body: formData
        }).then(async (response) => {
            // do something in the background
            dialog.modal('hide');
            let result = await response.text()
            console.log(result)
            if (result == 'success') {
                window.location = '/';
            }
        }).catch((error) => {
            console.log(error)
        });     
    });
}


initSubmitBtn();
queryAllHistoryMessage();