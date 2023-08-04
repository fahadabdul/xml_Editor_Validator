<schema xmlns="http://purl.oclc.org/dsdl/schematron">
    <pattern>
        <rule context="book">
            <assert test="title">the "title" element must be present.</assert>
            <assert test="author">the "author" element must be present.</assert>
        </rule>
    </pattern>
</schema>