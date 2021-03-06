from boost_site.util import htmlencode
emit('<ul class="toc">\n');

for x in downloads:
    emit('<li><a href="#%s">%s</a></li>\n' % (x['anchor'], x['label']))

emit('<li><a href="#history">Old Boost Releases</a></li>\n')
emit('<li><a href="#repository">Git Repositories</a></li>\n')
emit('</ul>\n')

for x in downloads:
    emit('<h2 id="%s">%s</h2>' % (x['anchor'], x['label']))
    for entry in x['entries']:
        emit('\n')
        emit('              <h3><span class=\n              "news-title">%s</span></h3>\n\n' % entry.full_title_xml)
        emit('              <p class="news-date">%s</p>\n\n' % entry.web_date())
        emit('              <p class="news-description">\n')
        emit('              <span class="brief"><span class="purpose">%s</span></span></p>\n\n' % entry.purpose_xml)
        emit('<ul class="menu">\n')
        emit('<li>')
        emit('<a href="/%s">Release Notes</a>' % htmlencode(entry.location))
        emit('</li>\n')
        if(entry.download_item):
            emit('<li>')
            emit('<a href="%s">Download</a>' % htmlencode(entry.download_item))
            emit('</li>\n')
        if(entry.documentation):
            emit('<li>')
            emit('<a href="%s">Documentation</a>' % htmlencode(entry.documentation))
            emit('</li>\n')
        emit('</ul>\n')
