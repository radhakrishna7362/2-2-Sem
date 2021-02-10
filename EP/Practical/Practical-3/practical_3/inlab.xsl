<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<html>
			<body>
				<h2>Books Information</h2>
				<table border="1" style="border-collapse:collapse">
					<tr bgcolor="#9acd32">
						<th>Title</th>
						<th>Author</th>
						<th>Publisher</th>
						<th>Edition</th>
						<th>Price</th>
					</tr>
					<xsl:for-each select="books/book">
						<tr>
							<td><xsl:value-of select="title"></xsl:value-of></td>
							<td><xsl:value-of select="author"></xsl:value-of></td>
							<td><xsl:value-of select="publisher"></xsl:value-of></td>
							<td><xsl:value-of select="edition"></xsl:value-of></td>
							<td><xsl:value-of select="price"></xsl:value-of></td>
						</tr>
					</xsl:for-each>
				</table>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>