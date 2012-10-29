$(function () {
  $('.fadeIn').delay(500).fadeIn();
  var flickInProgress = false;
  var flickToNextPageIfAny = function (currentPages, pagesToFlickTo, animation) {
    if (pagesToFlickTo.length <= 0 || flickInProgress) {
      return;
    }
    flickInProgress = true;
    pagesToFlickTo.addClass('opening');
    $('#notes .caption').fadeOut();
    var newPageNumber = pageNumberFrom(pagesToFlickTo);
    updatePermalink(newPageNumber);
    updateEoinLink(newPageNumber);
    animation(currentPages, pagesToFlickTo);
  };
  var updatePermalink = function (newPageNumber) {
    var isFirstPage = newPageNumber == 0;
    var newHref = isFirstPage ? "/mini-book/" : ("/mini-book/" + newPageNumber + ".." + (newPageNumber + 1));
    var newTitle = "Eoin Curran 1980 - 2010 : Memorial Book" + isFirstPage ? "" : " :: page " + newPageNumber + ".." + (newPageNumber + 1);
    window.history.replaceState({'pageNumber':newPageNumber}, newTitle, newHref);
  };
  var updateEoinLink = function (newPageNumber) {
    $('#eoin').attr('href', (newPageNumber == 0) ? "/" : "/mini-book");
  };
  var animateToNextPage = function (currentPages, pagesToFlickTo) {
    animatePageFlicking('right', 'left', currentPages, pagesToFlickTo);
  };
  var animateToPreviousPage = function (currentPages, pagesToFlickTo) {
    animatePageFlicking('left', 'right', currentPages, pagesToFlickTo);
  };
  var animatePageFlicking = function (from, to, currentPages, pagesToFlickTo) {
    var toDisappear = '.' + from + ' img';
    var toAppear = '.' + to + ' img';
    $(toDisappear, currentPages).animate({
      width:0
    }, 500, function () {
      updateCaptions(pagesToFlickTo);
      $(toAppear, pagesToFlickTo).css('width', 0);
      $(toAppear, pagesToFlickTo).css('z-index', 11);
      $(toAppear, pagesToFlickTo).animate({
        width:426
      }, 500, function () {
        currentPages.removeClass('opened');
        pagesToFlickTo.removeClass('opening');
        pagesToFlickTo.addClass('opened');
        $('img', pagesToFlickTo).css('z-index', 10);
        $('img', currentPages).css('z-index', 9);
        updatePageThickness(pagesToFlickTo);
        flickInProgress = false;
      });
    });
  };
  var updatePageThickness = function (pairOfPages) {
    var leftPage = pageNumberFrom(pairOfPages);
    var progress = 1;
    if (leftPage >= 40) {
      progress = 5;
    } else if (leftPage >= 30) {
      progress = 4
    } else if (leftPage >= 20) {
      progress = 3;
    } else if (leftPage >= 10) {
      progress = 2;
    }
    $('#memorial-book').attr('class', "progress-" + progress);
  };
  var updateCaptions = function (newPair) {
    $('#notes .caption').html("");
    var leftNote = $('a.left img', newPair).attr('alt') || "";
    var rightNote = $('a.right img', newPair).attr('alt') || "";
    if (leftNote == rightNote) {
      $('#notes .center').html(leftNote);
    } else {
      $('#notes .left').html(leftNote);
      $('#notes .right').html(rightNote);
    }
    $('#notes .caption').delay(200).fadeIn();
  };
  var pageNumberFrom = function (pages) {
    return parseInt(pages.attr('id').replace("page", ""), 10);
  };
  $('#memorial-book').bind('next', function () {
    var currentPages = $('.opened', this);
    flickToNextPageIfAny(currentPages, $(currentPages).next(), animateToNextPage);
  });
  $('#memorial-book').bind('previous', function () {
    var currentPages = $('.opened', this);
    flickToNextPageIfAny(currentPages, $(currentPages).prev(), animateToPreviousPage);
  });
  $('a.right').click(function () {
    $('#memorial-book').trigger('next');
    return false;
  });
  $('a.left').click(function () {
    $('#memorial-book').trigger('previous');
    return false;
  });
  var keyMap = {'J':'next', 'K':'previous', 37:"previous", 39:'next'};
  $(document).keydown(function (e) {
    var keyPressed = String.fromCharCode(e.keyCode);
    var event = keyMap[keyPressed];
    if (!event) {
      event = keyMap[e.keyCode];
    }
    if (event) {
      $('#memorial-book').trigger(event);
    }
  });
});
