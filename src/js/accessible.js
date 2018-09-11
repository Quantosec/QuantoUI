$(function() {
    setInterval(function() {
        $("i").each(function() {
                if ($(this).attr("symbol") != null) {
                    $(this).attr("aria-label", $(this).attr("symbol"));
                } else {
                    $(this).attr("aria-hidden", "true");
                }
            });
    }, 0);
});