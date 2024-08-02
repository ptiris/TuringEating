from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.structure import pages
import csv


template = """
???+ comments "*{score}* | {name}"
{content}
""".strip()

expert_url = "![](https://img.shields.io/badge/-Expert-blue?style=flat-square&color=rgb(127%2C%20161%2C%20195))"

class CommentsPlugin(BasePlugin):
    config_scheme = (
        ("enabled",config_options.Type(bool,default=True)),
        ("folded",config_options.Type(bool,default=False))
    )


    def on_config(self,config:config_options.Config):
        if not self.config.get("enabled"):
            return config
        with open("docs/data.csv","r",encoding="UTF-8") as f:
            csv_data = csv.DictReader(f)
            self.data = list(csv_data)

    def on_page_markdown(self,markdown,page:pages.Page,config: config_options.Config,files,**kwargs):
        if not self.config.get("enabled"):
            return markdown
        # if not page.meta.get("comments"):
        #     return markdown
        markdown = markdown.replace(
            "{{comments}}",
            self._get_page_markdown()
        )
        return markdown

    def _get_page_markdown(self)->str:
        markdown= ""
        pos_list = list(set(list(map(lambda x: x['位置'],self.data))))
        for pos in pos_list:
            markdown+=f"## {pos}\n\n"
            shops = list(filter(lambda x:x['位置']==pos,self.data))
            shops_list = list(set(list(map(lambda x: x['名称'],shops))))
            for shop in shops_list:
                markdown+=f"### {shop} \n\n"
                names = list(filter(lambda x:x['名称']==shop,shops))
                names_list = list(set(list(map(lambda x: x['名称'],names))))
                for name in names:
                    markdown+=template.format(
                        score = name['定位'],
                        name = name['姓名']+(expert_url if name['专家']=='True' else ''),
                        content = self._indent(name['评价'])
                    )+'\n'
                markdown+='\n'
            markdown+='\n'
        print(markdown)
        return markdown
    
    @staticmethod
    def _indent(text:str,amount=4):
        return "\n".join(" "*amount + line for line in text.splitlines())
