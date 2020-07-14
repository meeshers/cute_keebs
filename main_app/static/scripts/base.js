const modal = type => {
  $(`#${type}`)
      .modal({
          blurring: true
      })
      .modal('show');
};

/* Event Listener */
$('#login').on('click', () => modal('login-form'));
$('#sign-up').on('click', () => modal('signup-form'));
$('#create-case').on('click', () => modal('create-case-form'));

$('.special.cards .image').dimmer({
    on: 'hover'
  });
  