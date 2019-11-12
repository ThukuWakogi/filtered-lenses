let myNav = document.getElementById('nav-at-home')

window.onscroll = function() {
  'use strict'
  
  if (document.documentElement.scrollTop >= 200) myNav.classList.add('cstm-nav-bg-white')
  else myNav.classList.remove('cstm-nav-bg-white')
}
