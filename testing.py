from functions import *
from shapes import *
import algorithm1,algorithm2,algorithm3,algorithm4
import constants as const
from visualization import *
import ezdxf
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
import re
import glob

def dxf2arr( names, img_format='png', img_res=300):
    for name in names:
        doc = ezdxf.readfile(name)
        msp = doc.modelspace()
        # Recommended: audit & repair DXF document before rendering
        auditor = doc.audit()
        # The auditor.errors attribute stores severe errors,
        # which *may* raise exceptions when rendering.
        if len(auditor.errors) != 0:
            raise Exception("The DXF document is damaged and can't be converted!")
        else :
            fig = plt.figure()
            ax = fig.add_axes([0, 0, 1, 1])
            ctx = RenderContext(doc)
            ctx.set_current_layout(msp)
            ctx.current_layout.set_colors(bg='#FFFFFF')
            out = MatplotlibBackend(ax)
            Frontend(ctx, out).draw_layout(msp, finalize=True)

            img_name = re.findall("(\S+)\.",name)  # select the image name that is the same as the dxf file name
            first_param = ''.join(img_name) + img_format  #concatenate list and string
            fig.savefig(first_param, dpi=img_res)
            return png2arr(first_param)

arr2png(dxf2arr(['./IMG/c100.dxf'])).show()