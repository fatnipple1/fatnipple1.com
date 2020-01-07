window.onload = () => {
    document.body.style.background = 'black'
    document.body.style.margin = 0

    var wrapper = document.createElement('div')
    var player = document.createElement('iframe')

    wrapper.style.width = '100%'
    wrapper.style.height = '100%'

    player.style.width = '100%'
    player.style.height = '100%'

    var script = document.getElementById('player')
    var video_id = script.getAttribute('video')

    var params = [
        'autoplay=1',
        'autopause=0',
        'byline=0',
        'dnt=1',
        'fun=0',
        'loop=1',
        'muted=0',
        'portrait=0',
        'title=0',
        'transparent=1'
    ]

    player.setAttribute('src', `https://player.vimeo.com/video/${video_id}?${params.join('&')}`)
    player.setAttribute('frameborder', 0)
    player.setAttribute('allow', 'autoplay; fullscreen')

    wrapper.appendChild(player)

    document.body.appendChild(wrapper)
}