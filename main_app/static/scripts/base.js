const modal = type => {
  $(`#${type}`)
      .modal({
          blurring: true
      })
      .modal('show');
};

/* Event Listener */
$('#sign-in').on('click', () => modal('signin-form'));
$('#sign-up').on('click', () => modal('signup-form'));