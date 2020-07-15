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
$('#create-keycap').on('click', () => modal('create-keycap-form'));
$('#create-pcb').on('click', () => modal('create-pcb-form'));
$('#create-stab').on('click', () => modal('create-stab-form'));
$('#create-switch').on('click', () => modal('create-switch-form'));
$('#delete-confirm').on('click', () => modal('delete'));

$('#example2').calendar({
  type: 'date'
});

$('.special.cards .image').dimmer({
    on: 'hover'
  });
  