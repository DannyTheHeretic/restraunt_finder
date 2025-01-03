


async function add_favorite(id) {
    let response = await fetch(`/api/add_favorite?id=${id}`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
    });
    if (response.ok)
        location.reload();
    else
        console.error('Failed to get response from server');
}


async function remove_favorite(id) {
    let response = await fetch(`/api/remove_favorite?id=${id}`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
    });
    if (response.ok)
        location.reload();
    else
        console.error('Failed to get response from server');
}