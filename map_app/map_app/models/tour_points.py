from sqlalchemy import Column, String, Numeric, Boolean

from map_app.models.base import Base

class TourPoint(Base):
    """
    The database models for the tour points:

    Fields:
        latitude: Decimal. The tour point's latitude
        longitude: Decimal. The tour point's logintude
        name: String. The tour point's identification
        category: String. The tour point category
        user: String. The facebook id of the user which registered the tour point
        public: Boolean. Whether the display of this location in the app should be public or private
    """
    __tablename__ = "tour_points"

    latitude = Column(Numeric(precision=10, scale=8), primary_key=True)
    longitude = Column(Numeric(precision=10, scale=8), primary_key=True)
    name = Column(String(1024))
    category = Column(String(1024))
    user = Column(String(1024))
    public = Column(Boolean)



