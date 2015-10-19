/* dj_aa prefix: "Django add another" */

var dj_aa_overlay;
function dj_aa_showOverlay() {
  dj_aa_overlay = $('<div style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; background-color: black; opacity: 0.5; z-index: 9999;">');
  dj_aa_overlay.hide();
  dj_aa_overlay.appendTo(document.body);
  dj_aa_overlay.fadeIn('fast');
}

function dj_aa_closeOverlay() {
  if (dj_aa_overlay) {
    var overlay = dj_aa_overlay;
    dj_aa_overlay = null;
    overlay.fadeOut('fast', null, function () { overlay.remove(); });
  }
}

function dj_aa_popup() {
  dj_aa_showOverlay();

  var left   = (screen.width  / 2) - (popup_opts.width  / 2);
      top    = (screen.height / 2) - (popup_opts.height / 2);
  var win = window.open(
    popup_opts.url,
    null,
    'toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=yes, resizable=yes, copyhistory=no, width='+popup_opts.width+', height='+popup_opts.height+', top='+top+', left='+left
  );

  var maybeCloseOverlay = function () {
    if (!win || win.closed) {
      dj_aa_closeOverlay();
    } else {
      setTimeout(maybeCloseOverlay, 500);
    }
  }

  maybeCloseOverlay();

}

function dj_aa_addNewlyCreatedObject(objinfo) {
  try {
    var elem = document.getElementById(objinfo.target_elem);
    var o = new Option(objinfo.label, objinfo.id);
    elem.options[elem.options.length] = o;
    o.selected = true;
    $(elem).trigger("change");
  } catch (e) {
    alert(e);
  } finally {
    dj_aa_closeOverlay();
  }
}
